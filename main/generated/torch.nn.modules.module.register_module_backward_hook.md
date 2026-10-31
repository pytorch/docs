# torch.nn.modules.module.register_module_backward_hook

torch.nn.modules.module.register_module_backward_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/08c2d21eeac45d7bb2b95f497938e99c0250222d/torch/nn/modules/module.py#L296)

Register a backward hook common to all the modules.

This function is deprecated in favor of
[`torch.nn.modules.module.register_module_full_backward_hook()`](torch.nn.modules.module.register_module_full_backward_hook.html#torch.nn.modules.module.register_module_full_backward_hook)
and the behavior of this function will change in future versions.

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`