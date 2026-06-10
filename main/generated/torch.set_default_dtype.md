# torch.set_default_dtype

torch.set_default_dtype(*d*, */*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/__init__.py#L1335)

Sets the default floating point dtype to `d`. Supports floating point dtype
as inputs. Other dtypes will cause torch to raise an exception.

When PyTorch is initialized its default floating point dtype is torch.float32,
and the intent of set_default_dtype(torch.float64) is to facilitate NumPy-like
type inference. The default floating point dtype is used to:

1. Implicitly determine the default complex dtype. When the default floating type is float16,
the default complex dtype is complex32. For float32, the default complex dtype is complex64.
For float64, it is complex128. For bfloat16, an exception will be raised because
there is no corresponding complex type for bfloat16.
2. Infer the dtype for tensors constructed using Python floats or complex Python
numbers. See examples below.
3. Determine the result of type promotion between bool and integer tensors and
Python floats and complex Python numbers.

Parameters:

**d** ([`torch.dtype`](../tensor_attributes.html#torch.dtype)) - the floating point dtype to make the default.

Example

```
>>> # initial default for floating point is torch.float32
>>> # Python floats are interpreted as float32
>>> torch.tensor([1.2, 3]).dtype
torch.float32
>>> # initial default for floating point is torch.complex64
>>> # Complex Python numbers are interpreted as complex64
>>> torch.tensor([1.2, 3j]).dtype
torch.complex64
```

```
>>> torch.set_default_dtype(torch.float64)
>>> # Python floats are now interpreted as float64
>>> torch.tensor([1.2, 3]).dtype # a new floating point tensor
torch.float64
>>> # Complex Python numbers are now interpreted as complex128
>>> torch.tensor([1.2, 3j]).dtype # a new complex tensor
torch.complex128
```

```
>>> torch.set_default_dtype(torch.float16)
>>> # Python floats are now interpreted as float16
>>> torch.tensor([1.2, 3]).dtype # a new floating point tensor
torch.float16
>>> # Complex Python numbers are now interpreted as complex128
>>> torch.tensor([1.2, 3j]).dtype # a new complex tensor
torch.complex32
```