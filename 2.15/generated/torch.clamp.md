# torch.clamp

torch.clamp(*input*, *min=None*, *max=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Clamps all elements in `input` into the range [ [`min`](torch.min.html#torch.min), [`max`](torch.max.html#torch.max) ].
Letting min_value and max_value be [`min`](torch.min.html#torch.min) and [`max`](torch.max.html#torch.max), respectively, this returns:

yi=min⁡(max⁡(xi,min_valuei),max_valuei)y_i = \min(\max(x_i, \text{min\_value}_i), \text{max\_value}_i)

yi​=min(max(xi​,min_valuei​),max_valuei​)

If [`min`](torch.min.html#torch.min) is `None`, there is no lower bound.
Or, if [`max`](torch.max.html#torch.max) is `None` there is no upper bound.

Note

If [`min`](torch.min.html#torch.min) is greater than [`max`](torch.max.html#torch.max) `torch.clamp(..., min, max)`
sets all elements in `input` to the value of [`max`](torch.max.html#torch.max).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **min** (*Number**or*[*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - lower-bound of the range to be clamped to
- **max** (*Number**or*[*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - upper-bound of the range to be clamped to

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4)
>>> a
tensor([-1.7120, 0.1734, -0.0478, -0.0922])
>>> torch.clamp(a, min=-0.5, max=0.5)
tensor([-0.5000, 0.1734, -0.0478, -0.0922])

>>> min = torch.linspace(-1, 1, steps=4)
>>> torch.clamp(a, min=min)
tensor([-1.0000, 0.1734, 0.3333, 1.0000])
```