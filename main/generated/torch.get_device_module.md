# torch.get_device_module

torch.get_device_module(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/__init__.py#L2953)

Returns the module associated with a given device(e.g., torch.device('cuda'), "mtia:0", "xpu", ...).
If no device is given, return the module for the current accelerator or CPU if none is present.