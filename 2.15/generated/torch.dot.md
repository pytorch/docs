# torch.dot

torch.dot(*input*, *tensor*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the dot product of two 1D tensors.

Note

Unlike NumPy's dot, torch.dot intentionally only supports computing the dot product
of two 1D tensors with the same number of elements.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - first tensor in the dot product, must be 1D.
- **tensor** ([*Tensor*](../tensors.html#torch.Tensor)) - second tensor in the dot product, must be 1D.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.dot(torch.tensor([2, 3]), torch.tensor([2, 1]))
tensor(7)

>>> t1, t2 = torch.tensor([0, 1]), torch.tensor([2, 3])
>>> torch.dot(t1, t2)
tensor(3)
```