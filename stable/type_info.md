# Type Info

The numerical properties of a [`torch.dtype`](tensor_attributes.html#torch.dtype) can be accessed through either the `torch.finfo` or the `torch.iinfo`.

## torch.finfo

*class*torch.finfo

A `torch.finfo` is an object that represents the numerical properties of a floating point
[`torch.dtype`](tensor_attributes.html#torch.dtype), (i.e. `torch.float32`, `torch.float64`, `torch.float16`, and `torch.bfloat16`).
This is similar to [numpy.finfo](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html).

A `torch.finfo` provides the following attributes:

| Name | Type | Description |
| --- | --- | --- |
| bits | int | The number of bits occupied by the type. |
| eps | float | The difference between 1.0 and the next smallest representable float larger than 1.0. |
| max | float | The largest representable number. |
| min | float | The smallest representable number (typically `-max`). |
| tiny | float | The smallest positive normal number. Equivalent to `smallest_normal`. |
| smallest_normal | float | The smallest positive normal number. See notes. |
| resolution | float | The approximate decimal resolution of this type, i.e., `10**-precision`. |

Note

The constructor of `torch.finfo` can be called without argument,
in which case the class is created for the pytorch default dtype (as returned by [`torch.get_default_dtype()`](generated/torch.get_default_dtype.html#torch.get_default_dtype)).

Note

`smallest_normal` returns the smallest *normal* number, but there are smaller
subnormal numbers. See https://en.wikipedia.org/wiki/Denormal_number
for more information.

## torch.iinfo

*class*torch.iinfo

A `torch.iinfo` is an object that represents the numerical properties of a integer
[`torch.dtype`](tensor_attributes.html#torch.dtype) (i.e. `torch.uint8`, `torch.int8`, `torch.int16`, `torch.int32`, and `torch.int64`).
This is similar to [numpy.iinfo](https://numpy.org/doc/stable/reference/generated/numpy.iinfo.html).

A `torch.iinfo` provides the following attributes:

| Name | Type | Description |
| --- | --- | --- |
| bits | int | The number of bits occupied by the type. |
| max | int | The largest representable number. |
| min | int | The smallest representable number. |