# torch.accelerator.current_accelerator

torch.accelerator.current_accelerator(*check_available=False*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/accelerator/__init__.py#L103)

Return the device of the accelerator available at compilation time.
If no accelerator were available at compilation time, returns None.
See [accelerator](../torch.html#accelerators) for details.

Parameters:

**check_available** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if True, will also do a runtime check to see
if the device [`torch.accelerator.is_available()`](torch.accelerator.is_available.html#torch.accelerator.is_available) on top of the compile-time
check.
Default: `False`

Returns:

return the current accelerator as [`torch.device`](../tensor_attributes.html#torch.device).

Return type:

[torch.device](../tensor_attributes.html#torch.device)

Note

The index of the returned [`torch.device`](../tensor_attributes.html#torch.device) will be `None`, please use
[`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) to know the current index being used.
This API does NOT poison fork. For more details, see [Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note).

Example:

```
>>> # If an accelerator is available, sent the model to it
>>> model = torch.nn.Linear(2, 2)
>>> if (current_device := current_accelerator(check_available=True)) is not None:
>>> model.to(current_device)
```