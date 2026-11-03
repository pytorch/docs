# torch.nn.modules.module.register_module_full_backward_hook

torch.nn.modules.module.register_module_full_backward_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/fbab7cc90f5699714d5785aaa2f153c739435d6f/torch/nn/modules/module.py#L352)

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