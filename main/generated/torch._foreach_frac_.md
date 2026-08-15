# torch._foreach_frac_

torch._foreach_frac_(*self: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]

Applies [`torch.frac()`](torch.frac.html#torch.frac) in-place to each tensor in `self` and
returns `self`. The returned object is the exact list or tuple passed as input.