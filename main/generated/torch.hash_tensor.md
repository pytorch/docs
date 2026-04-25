# torch.hash_tensor

torch.hash_tensor(*input*, ***, *mode=0*) → [Tensor](../tensors.html#torch.Tensor)

Returns a hash of all elements in the `input` tensor.

Currently only mode=0 (reduction via xor) is supported. The output will always
be of type `torch.uint64`. The elements of `input` are upcasted to their
64 bit float / integer equivalent and bitcasted to `torch.uint64` before
reduction via xor.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**mode** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The hash to use. Default: 0 (xor_reduction)

Example:

```
>>> a = torch.randn(1, 3)
>>> a
tensor([[ 1.1918, -1.1813, 0.3373]])
>>> torch.hash_tensor(a)
tensor(13822780554648485888, dtype=torch.uint64)
```

torch.hash_tensor(*input*, *dim*, ***, *keepdim=False*, *mode=0*) → [Tensor](../tensors.html#torch.Tensor)

Returns the hash of each row of the `input` tensor in the given
dimension `dim` given by mode. If `dim` is a list of dimensions,
reduce over all of them.

If `keepdim` is `True`, the output tensor is of the same size
as `input` except in the dimension(s) `dim` where it is of size 1.
Otherwise, `dim` is squeezed (see [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)), resulting in the
output tensor having 1 (or `len(dim)`) fewer dimension(s).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**ints**,**optional*) - the dimension or dimensions to reduce.
If `None`, all dimensions are reduced.
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

**mode** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The hash to use. Default: 0 (xor_reduction)

Example:

```
>>> a = torch.randn(2, 4)
>>> a
tensor([[ 0.1317, -0.5554, -1.4724, -1.1391],
 [ 0.0778, -0.6070, 0.6375, 0.1798]])
>>> torch.hash_tensor(a, 1)
tensor([9233691267014066176, 9255993250844508160], dtype=torch.uint64)
```