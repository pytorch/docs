# Benchmark Utils - torch.utils.benchmark

*class*torch.utils.benchmark.Timer(*stmt='pass'*, *setup='pass'*, *global_setup=''*, *timer=<function timer>*, *globals=None*, *label=None*, *sub_label=None*, *description=None*, *env=None*, *num_threads=1*, *language=Language.PYTHON*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/timer.py#L66)

Helper class for measuring execution time of PyTorch statements.

For a full tutorial on how to use this class, see:
[https://pytorch.org/tutorials/recipes/recipes/benchmark.html](https://pytorch.org/tutorials/recipes/recipes/benchmark.html)

The PyTorch Timer is based on timeit.Timer (and in fact uses
timeit.Timer internally), but with several key differences:

1. Runtime aware:

Timer will perform warmups (important as some elements of PyTorch are
lazily initialized), set threadpool size so that comparisons are
apples-to-apples, and synchronize asynchronous accelerator functions when
necessary.
2. Focus on replicates:

When measuring code, and particularly complex kernels / models,
run-to-run variation is a significant confounding factor. It is
expected that all measurements should include replicates to quantify
noise and allow median computation, which is more robust than mean.
To that effect, this class deviates from the timeit API by
conceptually merging timeit.Timer.repeat and timeit.Timer.autorange.
(Exact algorithms are discussed in method docstrings.) The timeit
method is replicated for cases where an adaptive strategy is not
desired.
3. Optional metadata:

When defining a Timer, one can optionally specify label, sub_label,
description, and env. (Defined later) These fields are included in
the representation of result object and by the Compare class to group
and display results for comparison.
4. Instruction counts

In addition to wall times, Timer can run a statement under Callgrind
and report instructions executed.

Directly analogous to timeit.Timer constructor arguments:

> stmt, setup, timer, globals

PyTorch Timer specific constructor arguments:

> label, sub_label, description, env, num_threads

Parameters:

- **stmt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Code snippet to be run in a loop and timed.
- **setup** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Optional setup code. Used to define variables used in stmt
- **global_setup** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - (C++ only)
Code which is placed at the top level of the file for things like
#include statements.
- **timer** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[**]**,*[*float*](https://docs.python.org/3/library/functions.html#float)*]*) - Callable which returns the current time. If PyTorch was built
without accelerators or there is no accelerator present, this defaults to
timeit.default_timer; otherwise it will synchronize accelerators before
measuring the time.
- **globals** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|**None*) - A dict which defines the global variables when stmt is being
executed. This is the other method for providing variables which
stmt needs.
- **label** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None*) - String which summarizes stmt. For instance, if stmt is
"torch.nn.functional.relu(torch.add(x, 1, out=out))"
one might set label to "ReLU(x + 1)" to improve readability.
- **sub_label** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None*) -

Provide supplemental information to disambiguate measurements
with identical stmt or label. For instance, in our example
above sub_label might be "float" or "int", so that it is easy
to differentiate:
"ReLU(x + 1): (float)"

"ReLU(x + 1): (int)"
when printing Measurements or summarizing using Compare.
- **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None*) -

String to distinguish measurements with identical label and
sub_label. The principal use of description is to signal to
Compare the columns of data. For instance one might set it
based on the input size to create a table of the form:

```
| n=1 | n=4 | ...
 ------------- ...
ReLU(x + 1): (float) | ... | ... | ...
ReLU(x + 1): (int) | ... | ... | ...
```

using Compare. It is also included when printing a Measurement.
- **env** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None*) - This tag indicates that otherwise identical tasks were run in
different environments, and are therefore not equivalent, for
instance when A/B testing a change to a kernel. Compare will
treat Measurements with different env specification as distinct
when merging replicate runs.
- **num_threads** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The size of the PyTorch threadpool when executing stmt. Single
threaded performance is important as both a key inference workload
and a good indicator of intrinsic algorithmic efficiency, so the
default is set to one. This is in contrast to the default PyTorch
threadpool size which tries to utilize all cores.

adaptive_autorange(*threshold=0.1*, ***, *min_run_time=0.01*, *max_run_time=10.0*, *callback=None*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/timer.py#L384)

Similar to blocked_autorange but also checks for variablility in measurements
and repeats until iqr/median is smaller than threshold or max_run_time is reached.

At a high level, adaptive_autorange executes the following pseudo-code:

```
`setup`

times = []
while times.sum < max_run_time
 start = timer()
 for _ in range(block_size):
 `stmt`
 times.append(timer() - start)

 enough_data = len(times)>3 and times.sum > min_run_time
 small_iqr=times.iqr/times.mean<threshold

 if enough_data and small_iqr:
 break
```

Parameters:

- **threshold** ([*float*](https://docs.python.org/3/library/functions.html#float)) - value of iqr/median threshold for stopping
- **min_run_time** ([*float*](https://docs.python.org/3/library/functions.html#float)) - total runtime needed before checking threshold
- **max_run_time** ([*float*](https://docs.python.org/3/library/functions.html#float)) - total runtime for all measurements regardless of threshold

Returns:

A Measurement object that contains measured runtimes and
repetition counts, and can be used to compute statistics.
(mean, median, etc.)

Return type:

*Measurement*

blocked_autorange(*callback=None*, *min_run_time=0.2*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/timer.py#L324)

Measure many replicates while keeping timer overhead to a minimum.

At a high level, blocked_autorange executes the following pseudo-code:

```
`setup`

total_time = 0
while total_time < min_run_time
 start = timer()
 for _ in range(block_size):
 `stmt`
 total_time += (timer() - start)
```

Note the variable block_size in the inner loop. The choice of block
size is important to measurement quality, and must balance two
competing objectives:

> 1. A small block size results in more replicates and generally
> better statistics.
> 2. A large block size better amortizes the cost of timer
> invocation, and results in a less biased measurement. This is
> important because accelerator synchronization time is non-trivial
> (order single to low double digit microseconds) and would
> otherwise bias the measurement.

blocked_autorange sets block_size by running a warmup period,
increasing block size until timer overhead is less than 0.1% of
the overall computation. This value is then used for the main
measurement loop.

Returns:

A Measurement object that contains measured runtimes and
repetition counts, and can be used to compute statistics.
(mean, median, etc.)

Return type:

*Measurement*

collect_callgrind(*number: [int](https://docs.python.org/3/library/functions.html#int)*, ***, *repeats: [None](https://docs.python.org/3/library/constants.html#None)*, *collect_baseline: [bool](https://docs.python.org/3/library/functions.html#bool)*, *retain_out_file: [bool](https://docs.python.org/3/library/functions.html#bool)*) → CallgrindStats[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/timer.py#L469)

collect_callgrind(*number: [int](https://docs.python.org/3/library/functions.html#int)*, ***, *repeats: [int](https://docs.python.org/3/library/functions.html#int)*, *collect_baseline: [bool](https://docs.python.org/3/library/functions.html#bool)*, *retain_out_file: [bool](https://docs.python.org/3/library/functions.html#bool)*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[CallgrindStats, ...]

Collect instruction counts using Callgrind.

Unlike wall times, instruction counts are deterministic
(modulo non-determinism in the program itself and small amounts of
jitter from the Python interpreter.) This makes them ideal for detailed
performance analysis. This method runs stmt in a separate process
so that Valgrind can instrument the program. Performance is severely
degraded due to the instrumentation, however this is ameliorated by
the fact that a small number of iterations is generally sufficient to
obtain good measurements.

In order to use this method valgrind, callgrind_control, and
callgrind_annotate must be installed.

Because there is a process boundary between the caller (this process)
and the stmt execution, globals cannot contain arbitrary in-memory
data structures. (Unlike timing methods) Instead, globals are
restricted to builtins, nn.Modules's, and TorchScripted functions/modules
to reduce the surprise factor from serialization and subsequent
deserialization. The GlobalsBridge class provides more detail on this
subject. Take particular care with nn.Modules: they rely on pickle and
you may need to add an import to setup for them to transfer properly.

By default, a profile for an empty statement will be collected and
cached to indicate how many instructions are from the Python loop which
drives stmt.

Returns:

A CallgrindStats object which provides instruction counts and
some basic facilities for analyzing and manipulating results.

timeit(*number=1000000*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/timer.py#L259)

Mirrors the semantics of timeit.Timer.timeit().

Execute the main statement (stmt) number times.
[https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit](https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit)

Return type:

*Measurement*

*class*torch.utils.benchmark.Measurement(*number_per_run*, *raw_times*, *task_spec*, *metadata=None*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/common.py#L74)

The result of a Timer measurement.

This class stores one or more measurements of a given statement. It is
serializable and provides several convenience methods
(including a detailed __repr__) for downstream consumers.

*static*merge(*measurements*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/common.py#L230)

Convenience method for merging replicates.

Merge will extrapolate times to number_per_run=1 and will not
transfer any metadata. (Since it might differ between replicates)

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[Measurement]

*property*significant_figures*: [int](https://docs.python.org/3/library/functions.html#int)*

Approximate significant figure estimate.

This property is intended to give a convenient way to estimate the
precision of a measurement. It only uses the interquartile region to
estimate statistics to try to mitigate skew from the tails, and
uses a static z value of 1.645 since it is not expected to be used
for small values of n, so z can approximate t.

The significant figure estimation used in conjunction with the
trim_sigfig method to provide a more human interpretable data
summary. __repr__ does not use this method; it simply displays raw
values. Significant figure estimation is intended for Compare.

*class*torch.utils.benchmark.CallgrindStats(*task_spec*, *number_per_run*, *built_with_debug_symbols*, *baseline_inclusive_stats*, *baseline_exclusive_stats*, *stmt_inclusive_stats*, *stmt_exclusive_stats*, *stmt_callgrind_out*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L169)

Top level container for Callgrind results collected by Timer.

Manipulation is generally done using the FunctionCounts class, which is
obtained by calling CallgrindStats.stats(...). Several convenience
methods are provided as well; the most significant is
CallgrindStats.as_standardized().

as_standardized()[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L244)

Strip library names and some prefixes from function strings.

When comparing two different sets of instruction counts, on stumbling
block can be path prefixes. Callgrind includes the full filepath
when reporting a function (as it should). However, this can cause
issues when diffing profiles. If a key component such as Python
or PyTorch was built in separate locations in the two profiles, which
can result in something resembling:

```
23234231 /tmp/first_build_dir/thing.c:foo(...)
 9823794 /tmp/first_build_dir/thing.c:bar(...)
 ...
 53453 .../aten/src/Aten/...:function_that_actually_changed(...)
 ...
 -9823794 /tmp/second_build_dir/thing.c:bar(...)
-23234231 /tmp/second_build_dir/thing.c:foo(...)
```

Stripping prefixes can ameliorate this issue by regularizing the
strings and causing better cancellation of equivalent call sites
when diffing.

Return type:

*CallgrindStats*

counts(***, *denoise=False*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L218)

Returns the total number of instructions executed.

See FunctionCounts.denoise() for an explanation of the denoise arg.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

delta(*other*, *inclusive=False*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L227)

Diff two sets of counts.

One common reason to collect instruction counts is to determine the
the effect that a particular change will have on the number of instructions
needed to perform some unit of work. If a change increases that number, the
next logical question is "why". This generally involves looking at what part
if the code increased in instruction count. This function automates that
process so that one can easily diff counts on both an inclusive and
exclusive basis.

Return type:

*FunctionCounts*

stats(*inclusive=False*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L204)

Returns detailed function counts.

Conceptually, the FunctionCounts returned can be thought of as a tuple
of (count, path_and_function_name) tuples.

inclusive matches the semantics of callgrind. If True, the counts
include instructions executed by children. inclusive=True is useful
for identifying hot spots in code; inclusive=False is useful for
reducing noise when diffing counts from two different runs. (See
CallgrindStats.delta(...) for more details)

Return type:

*FunctionCounts*

*class*torch.utils.benchmark.FunctionCounts(*_data*, *inclusive*, *truncate_rows=True*, *_linewidth=None*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L44)

Container for manipulating Callgrind results.

It supports:

1. Addition and subtraction to combine or diff results.
2. Tuple-like indexing.
3. A denoise function which strips CPython calls which are known to
be non-deterministic and quite noisy.
4. Two higher order methods (filter and transform) for custom
manipulation.

denoise()[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L137)

Remove known noisy instructions.

Several instructions in the CPython interpreter are rather noisy. These
instructions involve unicode to dictionary lookups which Python uses to
map variable names. FunctionCounts is generally a content agnostic
container, however this is sufficiently important for obtaining
reliable results to warrant an exception.

Return type:

*FunctionCounts*

filter(*filter_fn*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L130)

Keep only the elements where filter_fn applied to function name returns True.

Return type:

FunctionCounts

transform(*map_fn*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/valgrind_wrapper/timer_interface.py#L117)

Apply map_fn to all of the function names.

This can be used to regularize function names (e.g. stripping irrelevant
parts of the file path), coalesce entries by mapping multiple functions
to the same name (in which case the counts are added together), etc.

Return type:

FunctionCounts

*class*torch.utils.benchmark.Compare(*results*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/compare.py#L269)

Helper class for displaying the results of many measurements in a
formatted table.

The table format is based on the information fields provided in
`torch.utils.benchmark.Timer` (description, label, sub_label,
num_threads, etc).

The table can be directly printed using `print()` or casted as a str.

For a full tutorial on how to use this class, see:
[https://pytorch.org/tutorials/recipes/recipes/benchmark.html](https://pytorch.org/tutorials/recipes/recipes/benchmark.html)

Parameters:

**results** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**Measurement**]*) - List of Measurement to display.

colorize(*rowwise=False*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/compare.py#L311)

Colorize formatted table.

Colorize columnwise by default.

extend_results(*results*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/compare.py#L295)

Append results to already stored ones.

All added results must be instances of `Measurement`.

highlight_warnings()[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/compare.py#L318)

Enables warning highlighting when building formatted table.

print()[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/compare.py#L322)

Print formatted table

trim_significant_figures()[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/utils/benchmark/utils/compare.py#L307)

Enables trimming of significant figures when building the formatted table.

# torch.utils.benchmark.examples

# torch.utils.benchmark.examples.spectral_ops_fuzz_test

Microbenchmarks for the torch.fft module

| [`run_benchmark`](generated/torch.utils.benchmark.examples.spectral_ops_fuzz_test.run_benchmark.html#torch.utils.benchmark.examples.spectral_ops_fuzz_test.run_benchmark) | |
| --- | --- |