# torch.accelerator.is_available

torch.accelerator.is_available()[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/accelerator/__init__.py#L73)

Check if the current accelerator is available at runtime: it was build, all the
required drivers are available and at least one device is visible.
See [accelerator](../torch.html#accelerators) for details.

Returns:

A boolean indicating if there is an available [accelerator](../torch.html#accelerators).

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

Note

This API delegates to the device-specific version of is_available.
On CUDA, when the environment variable `PYTORCH_NVML_BASED_CUDA_CHECK=1` is set,
this function will NOT poison fork. Otherwise, it will. For more details, see
[Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note).

Example:

```
>>> assert torch.accelerator.is_available() "No available accelerators detected."
```