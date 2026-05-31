# torch.from_dlpack

torch.from_dlpack(*ext_tensor*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/f7811aa3c052ace6751fbc2f6bc93908b9ea6b9f/torch/utils/dlpack.py#L58)

Converts a tensor from an external library into a `torch.Tensor`.

The returned PyTorch tensor will share the memory with the input tensor
(which may have come from another library). Note that in-place operations
will therefore also affect the data of the input tensor. This may lead to
unexpected issues (e.g., other libraries may have read-only flags or
immutable data structures), so the user should only do this if they know
for sure that this is fine.

Parameters:

- **ext_tensor** (object with `__dlpack__` attribute, or a DLPack capsule) -

The tensor or DLPack capsule to convert.

If `ext_tensor` is a tensor (or ndarray) object, it must support
the `__dlpack__` protocol (i.e., have a `ext_tensor.__dlpack__`
method). Otherwise `ext_tensor` may be a DLPack capsule, which is
an opaque `PyCapsule` instance, typically produced by a
`to_dlpack` function or method.
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*or**None*) - An optional PyTorch device
specifying where to place the new tensor. If None (default), the
new tensor will be on the same device as `ext_tensor`.
- **copy** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*or**None*) - An optional boolean indicating whether or not to copy
`self`. If None, PyTorch will copy only if necessary.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Examples:

```
>>> import torch.utils.dlpack
>>> t = torch.arange(4)

# Convert a tensor directly (supported in PyTorch >= 1.10)
>>> t2 = torch.from_dlpack(t)
>>> t2[:2] = -1 # show that memory is shared
>>> t2
tensor([-1, -1, 2, 3])
>>> t
tensor([-1, -1, 2, 3])

# The old-style DLPack usage, with an intermediate capsule object
>>> capsule = torch.utils.dlpack.to_dlpack(t)
>>> capsule
<capsule object "dltensor" at ...>
>>> t3 = torch.from_dlpack(capsule)
>>> t3
tensor([-1, -1, 2, 3])
>>> t3[0] = -9 # now we're sharing memory between 3 tensors
>>> t3
tensor([-9, -1, 2, 3])
>>> t2
tensor([-9, -1, 2, 3])
>>> t
tensor([-9, -1, 2, 3])
```