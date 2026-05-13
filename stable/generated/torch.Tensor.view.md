# torch.Tensor.view

Tensor.view(**shape*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the same data as the `self` tensor but of a
different [`shape`](torch.Tensor.shape.html#torch.Tensor.shape).

The returned tensor shares the same data and must have the same number
of elements, but may have a different size. For a tensor to be viewed, the new
view size must be compatible with its original size and stride, i.e., each new
view dimension must either be a subspace of an original dimension, or only span
across original dimensions d,d+1,...,d+kd, d+1, \dots, d+kd,d+1,...,d+k that satisfy the following
contiguity-like condition that ∀i=d,...,d+k−1\forall i = d, \dots, d+k-1∀i=d,...,d+k−1,

stride[i]=stride[i+1]×size[i+1]\text{stride}[i] = \text{stride}[i+1] \times \text{size}[i+1]stride[i]=stride[i+1]×size[i+1]

Otherwise, it will not be possible to view `self` tensor as [`shape`](torch.Tensor.shape.html#torch.Tensor.shape)
without copying it (e.g., via [`contiguous()`](torch.Tensor.contiguous.html#torch.Tensor.contiguous)). When it is unclear whether a
`view()` can be performed, it is advisable to use [`reshape()`](torch.reshape.html#torch.reshape), which
returns a view if the shapes are compatible, and copies (equivalent to calling
[`contiguous()`](torch.Tensor.contiguous.html#torch.Tensor.contiguous)) otherwise.

Parameters:

**shape** ([*torch.Size*](../size.html#torch.Size)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*...*) - the desired size

Example:

```
>>> x = torch.randn(4, 4)
>>> x.size()
torch.Size([4, 4])
>>> y = x.view(16)
>>> y.size()
torch.Size([16])
>>> z = x.view(-1, 8) # the size -1 is inferred from other dimensions
>>> z.size()
torch.Size([2, 8])

>>> a = torch.randn(1, 2, 3, 4)
>>> a.size()
torch.Size([1, 2, 3, 4])
>>> b = a.transpose(1, 2) # Swaps 2nd and 3rd dimension
>>> b.size()
torch.Size([1, 3, 2, 4])
>>> c = a.view(1, 3, 2, 4) # Does not change tensor layout in memory
>>> c.size()
torch.Size([1, 3, 2, 4])
>>> torch.equal(b, c)
False
```

view(*dtype*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the same data as the `self` tensor but of a
different [`dtype`](../tensor_attributes.html#torch.dtype).

If the element size of [`dtype`](../tensor_attributes.html#torch.dtype) is different than that of `self.dtype`,
then the size of the last dimension of the output will be scaled
proportionally. For instance, if [`dtype`](../tensor_attributes.html#torch.dtype) element size is twice that of
`self.dtype`, then each pair of elements in the last dimension of
`self` will be combined, and the size of the last dimension of the output
will be half that of `self`. If [`dtype`](../tensor_attributes.html#torch.dtype) element size is half that
of `self.dtype`, then each element in the last dimension of `self` will
be split in two, and the size of the last dimension of the output will be
double that of `self`. For this to be possible, the following conditions
must be true:

> - `self.dim()` must be greater than 0.
> - `self.stride(-1)` must be 1.

Additionally, if the element size of [`dtype`](../tensor_attributes.html#torch.dtype) is greater than that of
`self.dtype`, the following conditions must be true as well:

> - `self.size(-1)` must be divisible by the ratio between the element
> sizes of the dtypes.
> - `self.storage_offset()` must be divisible by the ratio between the
> element sizes of the dtypes.
> - The strides of all dimensions, except the last dimension, must be
> divisible by the ratio between the element sizes of the dtypes.

If any of the above conditions are not met, an error is thrown.

Warning

This overload is not supported by TorchScript, and using it in a Torchscript
program will cause undefined behavior.

Parameters:

**dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype)) - the desired dtype

Example:

```
>>> x = torch.randn(4, 4)
>>> x
tensor([[ 0.9482, -0.0310, 1.4999, -0.5316],
 [-0.1520, 0.7472, 0.5617, -0.8649],
 [-2.4724, -0.0334, -0.2976, -0.8499],
 [-0.2109, 1.9913, -0.9607, -0.6123]])
>>> x.dtype
torch.float32

>>> y = x.view(torch.int32)
>>> y
tensor([[ 1064483442, -1124191867, 1069546515, -1089989247],
 [-1105482831, 1061112040, 1057999968, -1084397505],
 [-1071760287, -1123489973, -1097310419, -1084649136],
 [-1101533110, 1073668768, -1082790149, -1088634448]],
 dtype=torch.int32)
>>> y[0, 0] = 1000000000
>>> x
tensor([[ 0.0047, -0.0310, 1.4999, -0.5316],
 [-0.1520, 0.7472, 0.5617, -0.8649],
 [-2.4724, -0.0334, -0.2976, -0.8499],
 [-0.2109, 1.9913, -0.9607, -0.6123]])

>>> x.view(torch.cfloat)
tensor([[ 0.0047-0.0310j, 1.4999-0.5316j],
 [-0.1520+0.7472j, 0.5617-0.8649j],
 [-2.4724-0.0334j, -0.2976-0.8499j],
 [-0.2109+1.9913j, -0.9607-0.6123j]])
>>> x.view(torch.cfloat).size()
torch.Size([4, 2])

>>> x.view(torch.uint8)
tensor([[ 0, 202, 154, 59, 182, 243, 253, 188, 185, 252, 191, 63, 240, 22,
 8, 191],
 [227, 165, 27, 190, 128, 72, 63, 63, 146, 203, 15, 63, 22, 106,
 93, 191],
 [205, 59, 30, 192, 112, 206, 8, 189, 7, 95, 152, 190, 12, 147,
 89, 191],
 [ 43, 246, 87, 190, 235, 226, 254, 63, 111, 240, 117, 191, 177, 191,
 28, 191]], dtype=torch.uint8)
>>> x.view(torch.uint8).size()
torch.Size([4, 16])
```