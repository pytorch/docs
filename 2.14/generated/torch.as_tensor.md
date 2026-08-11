# torch.as_tensor

torch.as_tensor(*data: Any*, ***, *dtype: [dtype](../tensor_attributes.html#torch.dtype) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *device: DeviceLikeType | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Converts `data` into a tensor, sharing data and preserving autograd
history if possible.

If `data` is already a tensor with the requested dtype and device
then `data` itself is returned, but if `data` is a
tensor with a different dtype or device then it's copied as if using
data.to(dtype=dtype, device=device).

If `data` is a NumPy array (an ndarray) with the same dtype and device then a
tensor is constructed using [`torch.from_numpy()`](torch.from_numpy.html#torch.from_numpy).

If `data` is a CuPy array, the returned tensor will be located on the same device as the CuPy array unless
specifically overwritten by [`device`](../tensor_attributes.html#torch.device) or a default device. The device of the CuPy array is inferred from the
pointer of the array using cudaPointerGetAttributes unless [`device`](../tensor_attributes.html#torch.device) is provided with an explicit device index.

See also

[`torch.tensor()`](torch.tensor.html#torch.tensor) never shares its data and creates a new "leaf tensor" (see [Autograd mechanics](../notes/autograd.html)).

Parameters:

- **data** (*array_like*) - Initial data for the tensor. Can be a list, tuple,
NumPy `ndarray`, scalar, and other types.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, infers data type from `data`.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the device of the constructed tensor. If None and data is a tensor
then the device of data is used. If None and data is not a tensor then
the result tensor is constructed on the current device.

Example:

```
>>> a = numpy.array([1, 2, 3])
>>> t = torch.as_tensor(a)
>>> t
tensor([ 1, 2, 3])
>>> t[0] = -1
>>> a
array([-1, 2, 3])

>>> a = numpy.array([1, 2, 3])
>>> t = torch.as_tensor(a, device=torch.device('cuda'))
>>> t
tensor([ 1, 2, 3])
>>> t[0] = -1
>>> a
array([1, 2, 3])
```