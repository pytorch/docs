# torch.accelerator.synchronize

torch.accelerator.synchronize(*device=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/accelerator/__init__.py#L247)

Wait for all kernels in all streams on the given device to complete.

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, optional) - device for which to synchronize. It must match
the current [accelerator](../torch.html#accelerators) device type. If not given,
use [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) by default.

Note

This function is a no-op if the current [accelerator](../torch.html#accelerators) is not initialized.

Example:

```
>>> assert torch.accelerator.is_available() "No available accelerators detected."
>>> start_event = torch.Event(enable_timing=True)
>>> end_event = torch.Event(enable_timing=True)
>>> start_event.record()
>>> tensor = torch.randn(100, device=torch.accelerator.current_accelerator())
>>> sum = torch.sum(tensor)
>>> end_event.record()
>>> torch.accelerator.synchronize()
>>> elapsed_time_ms = start_event.elapsed_time(end_event)
```