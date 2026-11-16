# torch.cuda.is_available

torch.cuda.is_available()[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/cuda/__init__.py#L222)

Return a bool indicating if CUDA is currently available.

Note

This function will NOT poison fork if the environment variable
`PYTORCH_NVML_BASED_CUDA_CHECK=1` is set. For more details, see
[Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note).

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)