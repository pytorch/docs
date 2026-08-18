# torch.nn.modules.module.register_module_backward_hook

torch.nn.modules.module.register_module_backward_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/nn/modules/module.py#L296)

Register a backward hook common to all the modules.

This function is deprecated in favor of
[`torch.nn.modules.module.register_module_full_backward_hook()`](torch.nn.modules.module.register_module_full_backward_hook.html#torch.nn.modules.module.register_module_full_backward_hook)
and the behavior of this function will change in future versions.

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`