# torch.accelerator.current_device_idx

torch.accelerator.current_device_idx()[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/accelerator/__init__.py#L134)

(Deprecated) Return the index of a currently selected device for the current [accelerator](../torch.html#accelerators).

Returns:

the index of a currently selected device.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Warning

`torch.accelerator.current_device_idx()` is deprecated in favor of [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index)
and will be removed in a future PyTorch release.