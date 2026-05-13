# TunableOp

## Overview

This module exposes a TunableOp interface.

Some operations, such as GEMMs, could be implemented using more than one library
or more than one technique. For example, a GEMM could be implemented for CUDA or
ROCm using either the blas or blasLt libraries. Further, ROCm's rocblas and
hipblaslt libraries allow the user to query for all possible algorithms and then
choose one. How does one know which implementation is the fastest and should be
chosen? That's what TunableOp provides.

### Enabling TunableOp and Tuning Separately

The TunableOp feature is enabled separately from enabling the tuning phase
itself. Enabling TunableOp means that PyTorch will replace any standard
operators with their Tunable implementations. Any call to a TunableOp first
checks whether it has already been tuned for the given operator inputs. If so,
it will immediately call the tuned operation; no further tuning will take place
even when the tuning setting is enabled. Instead if no tuning result is found,
and tuning is enabled, the TunableOp will benchmark every registered
implementation of that operator for the given set of inputs and select the
fastest.

### File Input and Output

The first time any TunableOp is invoked, the internal database of tuned
operations will be prepared by attempting to read the results from the given
file. The default filename is 'tunableop_results.csv'. To support tuning when
multiple GPUs are used across multiple processes, the GPU device ordinal is
automatically inserted into the filename to avoid multiple processes overwriting
the same file.

If tuning is enabled and new tunings are discovered during the course of your
workload, it will also write out to this same filename with all tunings, both
the ones it read in at startup as well as the new ones found at runtime. This
can be used, for example, to build up a tunings file across many workloads by
reusing the same file. The output file is automatically created when the
application terminates. This behavior can be controlled by the C++ and Python
APIs but not the environment variables.

Assuming you specified a filename, you'll end up with a CSV file with contents
like so:

```
Validator,PT_VERSION,2.2.0
Validator,ROCM_VERSION,6.0.0.0-12969-1544e39
Validator,HIPBLASLT_VERSION,0.6.0-a9c5cc7
Validator,ROCBLAS_VERSION,4.0.0-72e57364-dirty
GemmTunableOp_float_NT,nt_25088_4096_64,Gemm_Hipblaslt_1219,1.262
GemmTunableOp_float_NT,nt_4096_4096_64,Gemm_Rocblas_1216,0.033
```

Note the "Validator" lines. If you change a library version, or ROCm version, or
PyTorch version, TunableOp will detect this and reject the tunings file because
the prior tunings are likely affected by other software changes.

The remaining lines are the tuned solutions for each TunableOp encountered
during your execution. Each line consists of 4 comma-separated fields: operator
name, operator parameters, solution name, and average execution time. The
execution time is an optional field. The CSV file can be edited, but with
caution. For example, the solution name (field 3) can be changed to "Default"
and it will fall back to the original PyTorch untuned implementation. Or, in the
case of ROCm's hipBLAS or hipBLASLt libraries, if you know the specific solution
index you can override the solution that TunableOp selected by replacing the
value. The operator name and parameters (fields 1 and 2) are internally named
and should not be modified. In the case of GemmTunableOp, field 1 indicates the
datatype and whether the inputs are transposed (T) or not (N) and field 2
indicates the M, N, K input shapes.

There is an option to enable verbose output but it is only recommended for
debugging purposes. This will produce a lot of diagnostic messages but may be
useful to see if TunableOp is being used at all. Otherwise, TunableOp is
completely silent, besides file output, unless there is a warning or error
during its use. The verbose option is only available by setting the environment
variable PYTORCH_TUNABLEOP_VEROBSE=1.

### A Note on Tuning Behavior, Warmup, and Cache Effects

Tuning an operator consists of iterating through the list or registered
implementations and profiling each one. The profile is established by running a
single implementation in a loop multiple times and taking the average execution
time. There is also an optional warmup phase prior to tuning that can help with
reaching stable power states by the hardware. During tuning of a workload the
various hardware caches will more likely produce hits than when not tuning.
There are options for flushing the instruction cache and rotate the input tensors
which might help produce a more faithful profile of the tuned operator as if the
operator were run within a larger workload instead of in a tight, repetitive loop.

By default, each possible solution for a given operator will be run for either
100 iterations or as many iterations that can be run within 30ms, whichever is
smaller, and its average execution will be calculated. The fastest solution
among all that were successfully profiled will be chosen. A profile might fail
if the given solution doesn't achieve the same accuracy as the default
implementation or if the solution returns an error code.

### Current Tunable Operators

#### TunableGemm for ROCm

Currently only a TunableGemm for ROCm is implemented. Note that CUDA builds of
PyTorch will function correctly when using TunableOp but the only solution
available to CUDA builds is the 'Default' implementation i.e. the original
cuBLAS default, now called through TunableOp. Any call to at::cuda::blas::gemm()
or ::bgemm() will be routed through TunableOp when enabled. Calling gemm() for a
given set of input arguments (transa, transb, m, n, k) will attempt to use the
fastest available implementation across both rocblas and hipblaslt.

### Offline Tuning

#### Motivation

There are several use cases for offline tuning.

One use case involves a workload with a high-memory utilization, where regular tuning might lead to running out of memory.

Another use case is for compute-intensive workloads. In such cases, it is more resource-efficient to collect
the GEMMs for the workload once and then tune repeatedly with different tuning parameters or libraries.

#### Workflow

There are basically two steps:
1) Set the environment variables to collect the untuned GEMM and this will generate `tunableop_untuned0.csv`:

```
export PYTORCH_TUNABLEOP_ENABLED=1
export PYTORCH_TUNABLEOP_TUNING=0
export PYTORCH_TUNABLEOP_RECORD_UNTUNED=1
...
```

1. Run a Python script that reads the `tunableop_untuned0.csv` and generates the `tunableop_results0.csv`, like this:

```
import torch.cuda.tunable as tunable
import os

os.putenv("PYTORCH_TUNABLEOP_ENABLED", "1")
os.putenv("PYTORCH_TUNABLEOP_TUNING", "1")
os.putenv("PYTORCH_TUNABLEOP_RECORD_UNTUNED", "0")
tunable.tune_gemm_in_file("tunableop_untuned0.csv")
```

It is also possible to take multiple untuned files and distribute the GEMMs for tuning to multiple GPUs
within a single node. In the first step, the GEMMs are first gathered and duplicate GEMMs are eliminated.
Next, the GEMMs are distributed to different GPUs for tuning. After all GEMMs are tuned, the results from
all the GPUs are then gathered into a single file whose base filename has `_full0` appended to it
(for example `tunableop_results_full0.csv`). Finally, this new file, containing the gathered results, will be
duplicated N times, once for each GPU as convenience to the user will run the workload with the tuned
configuration on N GPUs.

```
if __name__ == "__main__":
 num_gpus = 8 # number of GPUs that will be used during the tuning process
 tunable.mgpu_tune_gemm_in_file("tunableop_untuned?.csv", num_gpus)
```

Note that the usage of the `mgpu_tune_gemm_in_file` API is different from its single GPU counterpart
(`tune_gemm_in_file`). The body of the Python script that calls the API must be wrapped in `main()` as shown
due to the use of concurrent futures module. The argument to `mgpu_tune_gemm_in_file` must contain a wild card
expression (`?` or `*`) to generate the list of untuned files containing the GEMMs to be processed. The `num_gpus`
must between 1 and the total number of GPUs available.

### Tuning Context

The behavior of TunableOp is currently manipulated through environment
variables, the C++ interface of at::cuda::tunable::getTuningContext(), or the
torch.cuda.tunable python interfaces. The environment variables take precedence
over any setting you manipulate using the C++ or Python APIs.

#### Environment Variable Interface

Environment variables are cached the first time they are read. You cannot use the
environment variable interface programmatically since the settings become fixed.
Use the C++ or Python APIs instead.

## API Reference

torch.cuda.tunable.enable(*val=True*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L217)

This is the big on/off switch for all TunableOp implementations.

torch.cuda.tunable.is_enabled()[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L222)

Returns whether the TunableOp feature is enabled.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.cuda.tunable.tuning_enable(*val=True*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L227)

Enable tuning of TunableOp implementations.

When enabled, if a tuned entry isn't found, run the tuning step and record
the entry.

torch.cuda.tunable.tuning_is_enabled()[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L236)

Returns whether TunableOp implementations can be tuned.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.cuda.tunable.record_untuned_enable(*val=True*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L241)

Enable recording untuned of TunableOp perations for offline tuning.

When enabled, if a tuned entry isn't found, write it to the untuned file.

torch.cuda.tunable.record_untuned_is_enabled()[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L249)

Returns whether TunableOp operations are recorded for offline tuning.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.cuda.tunable.set_max_tuning_duration(*duration*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L254)

Set max time in milliseconds to spend tuning a given solution.

If both max tuning duration and iterations are set, the smaller of the two
will be honored. At minimum 1 tuning iteration will always be run.

torch.cuda.tunable.get_max_tuning_duration()[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L263)

Get max time to spend tuning a given solution.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

torch.cuda.tunable.set_max_tuning_iterations(*iterations*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L268)

Set max number of iterations to spend tuning a given solution.

If both max tuning duration and iterations are set, the smaller of the two
will be honored. At minimum 1 tuning iteration will always be run.

torch.cuda.tunable.get_max_tuning_iterations()[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L277)

Get max iterations to spend tuning a given solution.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

torch.cuda.tunable.set_filename(*filename*, *insert_device_ordinal=False*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L282)

Set the filename to use for input/output of tuning results.

If `insert_device_ordinal` is `True` then the current device ordinal
will be added to the given filename automatically. This can be used in a
1-process-per-gpu scenario to ensure all processes write to a separate file.

torch.cuda.tunable.get_filename()[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L292)

Get the results filename.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

torch.cuda.tunable.get_results()[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L297)

Return all TunableOp results.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str), [float](https://docs.python.org/3/library/functions.html#float)]

torch.cuda.tunable.get_validators()[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L302)

Return the TunableOp validators.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]

torch.cuda.tunable.read_file(*filename=None*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L307)

Read results from a TunableOp CSV file.

If `filename` is not given, `get_filename()` is called.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.cuda.tunable.tune_gemm_in_file(*filename*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L337)

tune GEMM in file.

torch.cuda.tunable.mgpu_tune_gemm_in_file(*filename_pattern*, *num_gpus*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L797)

Process one or more files and distribute work over one or more GPUs.

torch.cuda.tunable.set_rotating_buffer_size(*buffer_size*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L317)

Set rotating buffer size to this value in MB, if the buffer size is greater than zero.

If less than zero, query L2 cache size. If equal to zero, means deactivate rotating buffer.

torch.cuda.tunable.get_rotating_buffer_size()[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L325)

Get the rotating buffer size in kilobytes.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

torch.cuda.tunable.set_numerical_check_tolerances(*enable*, *atol=1e-05*, *rtol=1e-05*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/cuda/tunable.py#L330)

Set the atol and rtol values in numeric check