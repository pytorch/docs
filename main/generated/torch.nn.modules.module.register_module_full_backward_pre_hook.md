# torch.nn.modules.module.register_module_full_backward_pre_hook

torch.nn.modules.module.register_module_full_backward_pre_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/007b142ea0da19b2a8b4c33c2544b0c2f459e7fc/torch/nn/modules/module.py#L324)

Register a backward pre-hook common to all the modules.

Warning

This adds global state to the nn.module module
and it is only intended for debugging/profiling purposes.

Hooks registered using this function behave in the same way as those
registered by [`torch.nn.Module.register_full_backward_pre_hook()`](torch.nn.Module.html#torch.nn.Module.register_full_backward_pre_hook).
Refer to its documentation for more details.

Hooks registered using this function will be called before hooks registered
using [`torch.nn.Module.register_full_backward_pre_hook()`](torch.nn.Module.html#torch.nn.Module.register_full_backward_pre_hook).

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`