# torch.get_device_module

torch.get_device_module(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/__init__.py#L3475)

Returns the module associated with a given device(e.g., torch.device('cuda'), "mtia:0", "xpu", ...).
If no device is given, return the module for the current accelerator or CPU if none is present.

Return type:

module