# torch.tril_indices

torch.tril_indices(*row*, *col*, *offset=0*, ***, *dtype=torch.long*, *device='cpu'*, *layout=torch.strided*) → [Tensor](../tensors.html#torch.Tensor)

Returns the indices of the lower triangular part of a `row`-by-
`col` matrix in a 2-by-N Tensor, where the first row contains row
coordinates of all indices and the second row contains column coordinates.
Indices are ordered based on rows and then columns.

The lower triangular part of the matrix is defined as the elements on and
below the diagonal.

The argument `offset` controls which diagonal to consider. If
`offset` = 0, all elements on and below the main diagonal are
retained. A positive value includes just as many diagonals above the main
diagonal, and similarly a negative value excludes just as many diagonals below
the main diagonal. The main diagonal are the set of indices
{(i,i)}\lbrace (i, i) \rbrace{(i,i)} for i∈[0,min⁡{d1,d2}−1]i \in [0, \min\{d_{1}, d_{2}\} - 1]i∈[0,min{d1​,d2​}−1]
where d1,d2d_{1}, d_{2}d1​,d2​ are the dimensions of the matrix.

Note

When running on CUDA, `row * col` must be less than 2592^{59}259 to
prevent overflow during calculation.

Parameters:

- **row** (`int`) - number of rows in the 2-D matrix.
- **col** (`int`) - number of columns in the 2-D matrix.
- **offset** (`int`) - diagonal offset from the main diagonal.
Default: if not provided, 0.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor,
only support `torch.int`, `torch.long`. Default: if `None`, `torch.long`.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). [`device`](../tensor_attributes.html#torch.device) will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - currently only support `torch.strided`.

Example:

```
>>> a = torch.tril_indices(3, 3)
>>> a
tensor([[0, 1, 1, 2, 2, 2],
 [0, 0, 1, 0, 1, 2]])

>>> a = torch.tril_indices(4, 3, -1)
>>> a
tensor([[1, 2, 2, 3, 3, 3],
 [0, 0, 1, 0, 1, 2]])

>>> a = torch.tril_indices(4, 3, 1)
>>> a
tensor([[0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3],
 [0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2]])
```