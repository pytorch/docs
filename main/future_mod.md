# torch.__future__

torch.__future__.set_overwrite_module_params_on_conversion(*value*)[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/__future__.py#L5)

Sets whether to assign new tensors to the parameters instead of changing the
existing parameters in-place when converting an `nn.Module`.

When enabled, the following methods will assign new parameters to the module:

1. `module.{device}()` (e.g. `nn.Module.cuda()`) for moving a module between devices
2. `module.{dtype}()` (e.g. `nn.Module.float()`) for converting a module to a different dtype
3. `nn.Module.to()`
4. `nn.Module.to_empty()`

Parameters:

**value** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to assign new tensors or not.

torch.__future__.get_overwrite_module_params_on_conversion()[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/__future__.py#L25)

Returns whether to assign new tensors to the parameters instead of changing the
existing parameters in-place when converting an [`torch.nn.Module`](generated/torch.nn.Module.html#torch.nn.Module). Defaults to `False`.

See `set_overwrite_module_params_on_conversion()` for more information.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.__future__.set_swap_module_params_on_conversion(*value*)[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/__future__.py#L35)

Sets whether to use [`swap_tensors()`](generated/torch.utils.swap_tensors.html#torch.utils.swap_tensors) instead of setting `.data` to
change the existing parameters in-place when converting an `nn.Module` and instead
of `param.copy_(state_dict[key])` when loading a state dict into an `nn.Module`.

Note

This function takes precedence over `get_overwrite_module_params_on_conversion()`

When enabled, the following methods will swap the existing parameters in-place:

1. `module.{device}()` (e.g. `nn.Module.cuda()`) for moving a module between devices
2. `module.{dtype}()` (e.g. `nn.Module.float()`) for converting a module to a different dtype
3. `nn.Module.to()`
4. `nn.Module.to_empty()`
5. `nn.Module.load_state_dict()`

The semantics for `load_state_dict()` when this is set are as follows:

1. For each parameter/buffer, its corresponding `state_dict['key']` is transformed via
[`module_load()`](generated/torch.Tensor.module_load.html#torch.Tensor.module_load) (i.e. `res = param.module_load(state_dict['key'])`)
2. If necessary, `res` will be wrapped in an `Parameter`
3. The parameter/buffer in the module will be swapped via [`swap_tensors()`](generated/torch.utils.swap_tensors.html#torch.utils.swap_tensors)
with `res`

Parameters:

**value** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to use [`swap_tensors()`](generated/torch.utils.swap_tensors.html#torch.utils.swap_tensors) or not.

torch.__future__.get_swap_module_params_on_conversion()[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/__future__.py#L68)

Returns whether to use [`swap_tensors()`](generated/torch.utils.swap_tensors.html#torch.utils.swap_tensors) instead of setting .data to
change the existing parameters in-place when converting an `nn.Module`. Defaults to `False`.

See `set_swap_module_params_on_conversion()` for more information.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)