# torch.set_default_tensor_type

torch.set_default_tensor_type(*t*, */*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/__init__.py#L1671)

Warning

This function is deprecated as of PyTorch 2.1, please use [`torch.set_default_dtype()`](torch.set_default_dtype.html#torch.set_default_dtype) and
[`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device) as alternatives.

Sets the default `torch.Tensor` type to floating point tensor type
`t`. This type will also be used as default floating point type for
type inference in [`torch.tensor()`](torch.tensor.html#torch.tensor).

The default floating point tensor type is initially `torch.FloatTensor`.

Parameters:

**t** ([*type*](https://docs.python.org/3/library/functions.html#type)*or**string*) - the floating point tensor type or its name

Example:

```
>>> torch.tensor([1.2, 3]).dtype # initial default for floating point is torch.float32
torch.float32
>>> torch.set_default_tensor_type(torch.DoubleTensor)
>>> torch.tensor([1.2, 3]).dtype # a new floating point tensor
torch.float64
```