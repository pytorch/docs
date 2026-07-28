# torch.accelerator.is_available

torch.accelerator.is_available()[[source]](https://github.com/pytorch/pytorch/blob/b7ee7397ead012835c2d80ee53f64800630b1ab9/torch/accelerator/__init__.py#L74)

Check if the current accelerator is available at runtime: it was built, all the
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