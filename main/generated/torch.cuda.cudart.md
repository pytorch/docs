# torch.cuda.cudart

torch.cuda.cudart()[[source]](https://github.com/pytorch/pytorch/blob/a37249c7e9824d557710fe7682d943593ef355d8/torch/cuda/__init__.py#L610)

Retrieves the CUDA runtime API module.

This function initializes the CUDA runtime environment if it is not already
initialized and returns the CUDA runtime API module (_cudart). The CUDA
runtime API module provides access to various CUDA runtime functions.

Parameters:

**None** -

Returns:

The CUDA runtime API module (_cudart).

Return type:

module

Raises:

- [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If CUDA cannot be re-initialized in a forked subprocess.
- [**AssertionError**](https://docs.python.org/3/library/exceptions.html#AssertionError) - If PyTorch is not compiled with CUDA support or if libcudart functions are unavailable.

Example of CUDA operations with profiling:

```
>>> import torch
>>> from torch.cuda import cudart, check_error
>>> import os
>>>
>>> os.environ["CUDA_PROFILE"] = "1"
>>>
>>> def perform_cuda_operations_with_streams():
>>> stream = torch.cuda.Stream()
>>> with torch.cuda.stream(stream):
>>> x = torch.randn(100, 100, device='cuda')
>>> y = torch.randn(100, 100, device='cuda')
>>> z = torch.mul(x, y)
>>> return z
>>>
>>> torch.cuda.synchronize()
>>> print("====== Start nsys profiling ======")
>>> check_error(cudart().cudaProfilerStart())
>>> with torch.autograd.profiler.emit_nvtx():
>>> result = perform_cuda_operations_with_streams()
>>> print("CUDA operations completed.")
>>> check_error(torch.cuda.cudart().cudaProfilerStop())
>>> print("====== End nsys profiling ======")
```

To run this example and save the profiling information, execute:

```
>>> $ nvprof --profile-from-start off --csv --print-summary -o trace_name.prof -f -- python cudart_test.py
```

This command profiles the CUDA operations in the provided script and saves
the profiling information to a file named trace_name.prof.
The -profile-from-start off option ensures that profiling starts only
after the cudaProfilerStart call in the script.
The -csv and -print-summary options format the profiling output as a
CSV file and print a summary, respectively.
The -o option specifies the output file name, and the -f option forces the
overwrite of the output file if it already exists.