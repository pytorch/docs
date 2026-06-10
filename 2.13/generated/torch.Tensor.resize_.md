# torch.Tensor.resize_

Tensor.resize_(**sizes*, *memory_format=torch.contiguous_format*) → [Tensor](../tensors.html#torch.Tensor)

Resizes `self` tensor to the specified size. If the number of elements is
larger than the current storage size, then the underlying storage is resized
to fit the new number of elements. If the number of elements is smaller, the
underlying storage is not changed. Existing elements are preserved but any new
memory is uninitialized.

Warning

This is a low-level method. The storage is reinterpreted as C-contiguous,
ignoring the current strides (unless the target size equals the current
size, in which case the tensor is left unchanged). For most purposes, you
will instead want to use [`view()`](torch.Tensor.view.html#torch.Tensor.view), which checks for
contiguity, or [`reshape()`](torch.Tensor.reshape.html#torch.Tensor.reshape), which copies data if needed. To
change the size in-place with custom strides, see [`set_()`](torch.Tensor.set_.html#torch.Tensor.set_).

Note

If [`torch.use_deterministic_algorithms()`](torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms) and
[`torch.utils.deterministic.fill_uninitialized_memory`](../deterministic.html#torch.utils.deterministic.fill_uninitialized_memory) are both set to
`True`, new elements are initialized to prevent nondeterministic behavior
from using the result as an input to an operation. Floating point and
complex values are set to NaN, and integer values are set to the maximum
value.

Parameters:

- **sizes** ([*torch.Size*](../size.html#torch.Size)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*...*) - the desired size
- **memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
Tensor. Default: `torch.contiguous_format`. Note that memory format of
`self` is going to be unaffected if `self.size()` matches `sizes`.

Example:

```
>>> x = torch.tensor([[1, 2], [3, 4], [5, 6]])
>>> x.resize_(2, 2)
tensor([[ 1, 2],
 [ 3, 4]])
```