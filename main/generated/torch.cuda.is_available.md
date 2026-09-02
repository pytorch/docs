# torch.cuda.is_available

torch.cuda.is_available()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/__init__.py#L209)

Return a bool indicating if CUDA is currently available.

Note

This function will NOT poison fork if the environment variable
`PYTORCH_NVML_BASED_CUDA_CHECK=1` is set. For more details, see
[Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note).

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)