# torch.get_device_module

torch.get_device_module(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/__init__.py#L3425)

Returns the module associated with a given device(e.g., torch.device('cuda'), "mtia:0", "xpu", ...).
If no device is given, return the module for the current accelerator or CPU if none is present.

Return type:

module