# torch.accelerator.get_device_capability

torch.accelerator.get_device_capability(*device=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/accelerator/__init__.py#L162)

Return the capability of the currently selected device.

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, optional) - The device to query capabilities for
[accelerator](../torch.html#accelerators) device type. If not given,
use [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) by default.

Returns:

A dictionary containing device capability information. The dictionary includes:

- `supported_dtypes` (set(torch.dtype)): Set of PyTorch data types for which
tensors can be allocated on the accelerator and type conversion across
supported dtypes are supported. Any operator support outside of that
is not guaranteed

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Any]

Examples

```
>>> # Query capabilities for current device
>>> capabilities = torch.accelerator.get_device_capability("cuda:0")
>>> print("Supported dtypes:", capabilities["supported_dtypes"])
```