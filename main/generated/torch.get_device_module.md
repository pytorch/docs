# torch.get_device_module

torch.get_device_module(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/__init__.py#L3504)

Returns the module associated with a given device(e.g., torch.device('cuda'), "mtia:0", "xpu", ...).
If no device is given, return the module for the current accelerator or CPU if none is present.

Return type:

module