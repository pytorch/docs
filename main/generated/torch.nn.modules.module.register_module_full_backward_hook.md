# torch.nn.modules.module.register_module_full_backward_hook

torch.nn.modules.module.register_module_full_backward_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/nn/modules/module.py#L352)

Register a backward hook common to all the modules.

Warning

This adds global state to the nn.module module
and it is only intended for debugging/profiling purposes.

Hooks registered using this function behave in the same way as those
registered by [`torch.nn.Module.register_full_backward_hook()`](torch.nn.Module.html#torch.nn.Module.register_full_backward_hook).
Refer to its documentation for more details.

Hooks registered using this function will be called before hooks registered
using [`torch.nn.Module.register_full_backward_hook()`](torch.nn.Module.html#torch.nn.Module.register_full_backward_hook).

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`