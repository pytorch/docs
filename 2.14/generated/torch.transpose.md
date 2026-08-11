# torch.transpose

torch.transpose(*input*, *dim0*, *dim1*) → [Tensor](../tensors.html#torch.Tensor)

Returns a tensor that is a transposed version of `input`.
The given dimensions `dim0` and `dim1` are swapped.

If `input` is a strided tensor then the resulting `out`
tensor shares its underlying storage with the `input` tensor, so
changing the content of one would change the content of the other.

If `input` is a [sparse tensor](../sparse.html#sparse-docs) then the
resulting `out` tensor *does not* share the underlying storage
with the `input` tensor.

If `input` is a [sparse tensor](../sparse.html#sparse-docs) with compressed
layout (SparseCSR, SparseBSR, SparseCSC or SparseBSC) the arguments
`dim0` and `dim1` must be both batch dimensions, or must
both be sparse dimensions. The batch dimensions of a sparse tensor are the
dimensions preceding the sparse dimensions.

Note

Transpositions which interchange the sparse dimensions of a SparseCSR
or SparseCSC layout tensor will result in the layout changing between
the two options. Transposition of the sparse dimensions of a ` SparseBSR`
or SparseBSC layout tensor will likewise generate a result with the
opposite layout.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim0** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the first dimension to be transposed
- **dim1** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the second dimension to be transposed

Example:

```
>>> x = torch.randn(2, 3)
>>> x
tensor([[ 1.0028, -0.9893, 0.5809],
 [-0.1669, 0.7299, 0.4942]])
>>> torch.transpose(x, 0, 1)
tensor([[ 1.0028, -0.1669],
 [-0.9893, 0.7299],
 [ 0.5809, 0.4942]])
```

See also [`torch.t()`](torch.t.html#torch.t).