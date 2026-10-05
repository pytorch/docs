# torch.logical_and

torch.logical_and(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the element-wise logical AND of the given input tensors. Zeros are treated as `False` and nonzeros are
treated as `True`.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor to compute AND with

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.logical_and(torch.tensor([True, False, True]), torch.tensor([True, False, False]))
tensor([ True, False, False])
>>> a = torch.tensor([0, 1, 10, 0], dtype=torch.int8)
>>> b = torch.tensor([4, 0, 1, 0], dtype=torch.int8)
>>> torch.logical_and(a, b)
tensor([False, False, True, False])
>>> torch.logical_and(a.double(), b.double())
tensor([False, False, True, False])
>>> torch.logical_and(a.double(), b)
tensor([False, False, True, False])
>>> torch.logical_and(a, b, out=torch.empty(4, dtype=torch.bool))
tensor([False, False, True, False])
```