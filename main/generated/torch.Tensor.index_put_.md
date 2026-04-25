# torch.Tensor.index_put_

Tensor.index_put_(*indices*, *values*, *accumulate=False*) → [Tensor](../tensors.html#torch.Tensor)

Puts values from the tensor [`values`](torch.Tensor.values.html#torch.Tensor.values) into the tensor `self` using
the indices specified in [`indices`](torch.Tensor.indices.html#torch.Tensor.indices) (which is a tuple of Tensors). The
expression `tensor.index_put_(indices, values)` is equivalent to
`tensor[indices] = values`. Returns `self`.

If `accumulate` is `True`, the elements in [`values`](torch.Tensor.values.html#torch.Tensor.values) are added to
`self`. If accumulate is `False`, the behavior is undefined if indices
contain duplicate elements.

Parameters:

- **indices** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**LongTensor*) - tensors used to index into self.
- **values** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of same dtype as self.
- **accumulate** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - whether to accumulate into self