# torch.kthvalue

torch.kthvalue(*input*, *k*, *dim=None*, *keepdim=False*, ***, *out=None*)

Returns a namedtuple `(values, indices)` where `values` is the `k` th
smallest element of each row of the `input` tensor in the given dimension
`dim`. And `indices` is the index location of each element found.

If `dim` is not given, the last dimension of the input is chosen.

If `keepdim` is `True`, both the `values` and `indices` tensors
are the same size as `input`, except in the dimension `dim` where
they are of size 1. Otherwise, `dim` is squeezed
(see [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)), resulting in both the `values` and
`indices` tensors having 1 fewer dimension than the `input` tensor.

Note

When `input` is a CUDA tensor and there are multiple valid
`k` th values, this function may nondeterministically return
`indices` for any of them.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **k** ([*int*](https://docs.python.org/3/library/functions.html#int)) - k for the k-th smallest element
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the dimension to find the kth value along
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

**out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - the output tuple of (Tensor, LongTensor)
can be optionally given to be used as output buffers

Example:

```
>>> x = torch.arange(1., 6.)
>>> x
tensor([ 1., 2., 3., 4., 5.])
>>> torch.kthvalue(x, 4)
torch.return_types.kthvalue(values=tensor(4.), indices=tensor(3))

>>> x=torch.arange(1.,7.).resize_(2,3)
>>> x
tensor([[ 1., 2., 3.],
 [ 4., 5., 6.]])
>>> torch.kthvalue(x, 2, 0, True)
torch.return_types.kthvalue(values=tensor([[4., 5., 6.]]), indices=tensor([[1, 1, 1]]))
```