# torch.Tensor.type

Tensor.type(*dtype=None*, *non_blocking=False*, ***kwargs*) → str or Tensor

Returns the type if dtype is not provided, else casts this object to
the specified type.

If this is already of the correct type, no copy is performed and the
original object is returned.

Parameters:

- **dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)*or**string*) - The desired type
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True`, and the source is in pinned memory
and destination is on the GPU or vice versa, the copy is performed
asynchronously with respect to the host. Otherwise, the argument
has no effect.
- ****kwargs** - For compatibility, may contain the key `async` in place of
the `non_blocking` argument. The `async` arg is deprecated.