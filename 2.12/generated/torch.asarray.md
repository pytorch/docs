# torch.asarray

torch.asarray(*obj: Any*, ***, *dtype: [dtype](../tensor_attributes.html#torch.dtype) | [None](https://docs.python.org/3/library/constants.html#None)*, *device: DeviceLikeType | [None](https://docs.python.org/3/library/constants.html#None)*, *copy: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *requires_grad: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None) = None*) → [Tensor](../tensors.html#torch.Tensor)

Converts `obj` to a tensor.

`obj` can be one of:

1. a tensor
2. a NumPy array or a NumPy scalar
3. a DLPack capsule
4. an object that implements Python's buffer protocol
5. a scalar
6. a sequence of scalars

When `obj` is a tensor, NumPy array, or DLPack capsule the returned tensor will,
by default, have the same requires_grad as `obj` (defaulting to False), have the
same datatype, be on the same device, and share memory with it. These properties can be
controlled with the [`dtype`](../tensor_attributes.html#torch.dtype), [`device`](../tensor_attributes.html#torch.device), `copy`, and
`requires_grad` keyword arguments. If the returned tensor is of a different
datatype, on a different device, or a copy is requested then it will not share its
memory with `obj`. If `requires_grad` is `True` (or `None`, and
`obj` was a tensor with requires_grad set), then the returned tensor will require
a gradient, and if `obj` is also a tensor with an autograd history then the
returned tensor will have the same history.

When `obj` is not a tensor, NumPy array, or DLPack capsule but implements Python's
buffer protocol then the buffer is interpreted as an array of bytes grouped according to
the size of the datatype passed to the [`dtype`](../tensor_attributes.html#torch.dtype) keyword argument. (If no datatype is
passed then the default floating point datatype is used, instead.) The returned tensor
will have the specified datatype (or default floating point datatype if none is specified)
and, by default, be on the CPU device and share memory with the buffer.

When `obj` is a NumPy scalar, the returned tensor will be a 0-dimensional tensor on
the CPU and that doesn't share its memory (i.e. `copy=True`). By default datatype will
be the PyTorch datatype corresponding to the NumPy's scalar's datatype.

When `obj` is none of the above but a scalar, or a sequence of scalars then the
returned tensor will, by default, infer its datatype from the scalar values, be on the
current default device, and not share its memory.

See also

[`torch.tensor()`](torch.tensor.html#torch.tensor) creates a tensor that always copies the data from the input object.
[`torch.from_numpy()`](torch.from_numpy.html#torch.from_numpy) creates a tensor that always shares memory from NumPy arrays.
[`torch.frombuffer()`](torch.frombuffer.html#torch.frombuffer) creates a tensor that always shares memory from objects that
implement the buffer protocol.
[`torch.from_dlpack()`](torch.from_dlpack.html#torch.from_dlpack) creates a tensor that always shares memory from
DLPack capsules.

Parameters:

**obj** ([*object*](https://docs.python.org/3/library/functions.html#object)) - a tensor, NumPy array, DLPack Capsule, object that implements Python's
buffer protocol, scalar, or sequence of scalars.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the datatype of the returned tensor.
Default: `None`, which causes the datatype of the returned tensor to be
inferred from `obj`.
- **copy** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - controls whether the returned tensor shares memory with `obj`.
Default: `None`, which causes the returned tensor to share memory with `obj`
whenever possible. If `True` then the returned tensor does not share its memory.
If `False` then the returned tensor shares its memory with `obj` and an
error is thrown if it cannot.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the device of the returned tensor.
Default: `None`, which causes the device of `obj` to be used. Or, if
`obj` is a Python sequence, the current default device will be used.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the returned tensor requires grad.
Default: `None`, which causes requires_grad for the returned tensor to be
inferred from `obj`. If `True`, then the returned tensor will require
a gradient, and if `obj` is also a tensor with an autograd history then
the returned tensor will have the same history.

Example:

```
>>> a = torch.tensor([1, 2, 3])
>>> # Shares memory with tensor 'a'
>>> b = torch.asarray(a)
>>> a.data_ptr() == b.data_ptr()
True
>>> # Forces memory copy
>>> c = torch.asarray(a, copy=True)
>>> a.data_ptr() == c.data_ptr()
False

>>> a = torch.tensor([1., 2., 3.], requires_grad=True)
>>> b = a + 2
>>> b
tensor([3., 4., 5.], grad_fn=<AddBackward0>)
>>> # Shares memory with tensor 'b', with no grad
>>> c = torch.asarray(b, requires_grad=False)
>>> c
tensor([3., 4., 5.])
>>> # Shares memory with tensor 'b', retaining autograd history
>>> d = torch.asarray(b, requires_grad=True)
>>> d
tensor([3., 4., 5.], grad_fn=<AddBackward0>)
>>> # Shares memory with tensor 'b', retaining autograd history
>>> e = torch.asarray(b)
>>> e
tensor([3., 4., 5.], grad_fn=<AddBackward0>)

>>> array = numpy.array([1, 2, 3])
>>> # Shares memory with array 'array'
>>> t1 = torch.asarray(array)
>>> array.__array_interface__['data'][0] == t1.data_ptr()
True
>>> # Copies memory due to dtype mismatch
>>> t2 = torch.asarray(array, dtype=torch.float32)
>>> array.__array_interface__['data'][0] == t2.data_ptr()
False

>>> scalar = numpy.float64(0.5)
>>> torch.asarray(scalar)
tensor(0.5000, dtype=torch.float64)
```