# torch.Tensor.module_load

Tensor.module_load(*other*, *assign=False*)[[source]](https://github.com/pytorch/pytorch/blob/9179f2014ca7f941551131fc2315cfcf9e206bd3/torch/_tensor.py#L849)

Defines how to transform `other` when loading it into `self` in [`load_state_dict()`](torch.nn.Module.html#torch.nn.Module.load_state_dict).

Used when [`get_swap_module_params_on_conversion()`](../future_mod.html#torch.__future__.get_swap_module_params_on_conversion) is `True`.

It is expected that `self` is a parameter or buffer in an `nn.Module` and `other` is the
value in the state dictionary with the corresponding key, this method defines
how `other` is remapped before being swapped with `self` via
[`swap_tensors()`](torch.utils.swap_tensors.html#torch.utils.swap_tensors) in [`load_state_dict()`](torch.nn.Module.html#torch.nn.Module.load_state_dict).

Note

This method should always return a new object that is not `self` or `other`.
For example, the default implementation returns `self.copy_(other).detach()`
if `assign` is `False` or `other.detach()` if `assign` is `True`.

Parameters:

- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - value in state dict with key corresponding to `self`
- **assign** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - the assign argument passed to [`nn.Module.load_state_dict()`](torch.nn.Module.html#torch.nn.Module.load_state_dict)