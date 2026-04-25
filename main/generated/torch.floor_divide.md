# torch.floor_divide

torch.floor_divide(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Note

Before PyTorch 1.13 `torch.floor_divide()` incorrectly performed
truncation division. To restore the previous behavior use
[`torch.div()`](torch.div.html#torch.div) with `rounding_mode='trunc'`.

Computes `input` divided by `other`, elementwise, and floors
the result.

outi=floor(inputiotheri)\text{{out}}_i = \text{floor} \left( \frac{{\text{{input}}_i}}{{\text{{other}}_i}} \right)

outi​=floor(otheri​inputi​​)

Supports broadcasting to a common shape, type promotion, and integer and float inputs.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)*or**Number*) - the dividend
- **other** ([*Tensor*](../tensors.html#torch.Tensor)*or**Number*) - the divisor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([4.0, 3.0])
>>> b = torch.tensor([2.0, 2.0])
>>> torch.floor_divide(a, b)
tensor([2.0, 1.0])
>>> torch.floor_divide(a, 1.4)
tensor([2.0, 2.0])
```