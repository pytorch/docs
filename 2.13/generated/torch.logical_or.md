# torch.logical_or

torch.logical_or(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the element-wise logical OR of the given input tensors. Zeros are treated as `False` and nonzeros are
treated as `True`.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor to compute OR with

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.logical_or(torch.tensor([True, False, True]), torch.tensor([True, False, False]))
tensor([ True, False, True])
>>> a = torch.tensor([0, 1, 10, 0], dtype=torch.int8)
>>> b = torch.tensor([4, 0, 1, 0], dtype=torch.int8)
>>> torch.logical_or(a, b)
tensor([ True, True, True, False])
>>> torch.logical_or(a.double(), b.double())
tensor([ True, True, True, False])
>>> torch.logical_or(a.double(), b)
tensor([ True, True, True, False])
>>> torch.logical_or(a, b, out=torch.empty(4, dtype=torch.bool))
tensor([ True, True, True, False])
```