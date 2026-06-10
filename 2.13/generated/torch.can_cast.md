# torch.can_cast

torch.can_cast(*from_*, *to*) → [bool](https://docs.python.org/3/library/functions.html#bool)

Determines if a type conversion is allowed under PyTorch casting rules
described in the type promotion [documentation](../tensor_attributes.html#type-promotion-doc).

Parameters:

- **from_** ([*dtype*](../tensor_attributes.html#torch.dtype)) - The original [`torch.dtype`](../tensor_attributes.html#torch.dtype).
- **to** ([*dtype*](../tensor_attributes.html#torch.dtype)) - The target [`torch.dtype`](../tensor_attributes.html#torch.dtype).

Example:

```
>>> torch.can_cast(torch.double, torch.float)
True
>>> torch.can_cast(torch.float, torch.int)
False
```