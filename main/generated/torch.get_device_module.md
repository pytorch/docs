# torch.get_device_module

torch.get_device_module(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/__init__.py#L3478)

Returns the module associated with a given device(e.g., torch.device('cuda'), "mtia:0", "xpu", ...).
If no device is given, return the module for the current accelerator or CPU if none is present.

Return type:

module