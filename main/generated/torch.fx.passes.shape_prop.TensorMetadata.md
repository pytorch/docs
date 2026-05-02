# TensorMetadata

*class*torch.fx.passes.shape_prop.TensorMetadata(*shape*, *dtype*, *requires_grad*, *stride*, *memory_format*, *is_quantized*, *qparams*)[[source]](https://github.com/pytorch/pytorch/blob/7b5f32b1c4911f959ed9f61cd0aefb7ed57e0317/torch/fx/passes/shape_prop.py#L17)

A structure containing pertinent information about a tensor within a PyTorch program.

Note

Backwards-compatibility for this API is guaranteed.

count(*value*, */*)

Return number of occurrences of value.

dtype*: [dtype](../tensor_attributes.html#torch.dtype)*

Alias for field number 1

index(*value*, *start=0*, *stop=9223372036854775807*, */*)

Return first index of value.

Raises ValueError if the value is not present.

is_quantized*: [bool](https://docs.python.org/3/library/functions.html#bool)*

Alias for field number 5

memory_format*: [memory_format](../tensor_attributes.html#torch.memory_format) | [None](https://docs.python.org/3/library/constants.html#None)*

Alias for field number 4

qparams*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]*

Alias for field number 6

requires_grad*: [bool](https://docs.python.org/3/library/functions.html#bool)*

Alias for field number 2

shape*: [Size](../size.html#torch.Size)*

Alias for field number 0

stride*: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), ...]*

Alias for field number 3