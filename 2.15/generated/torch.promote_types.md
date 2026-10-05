# torch.promote_types

torch.promote_types(*type1*, *type2*) → [dtype](../tensor_attributes.html#torch.dtype)

Returns the [`torch.dtype`](../tensor_attributes.html#torch.dtype) with the smallest size and scalar kind that is
not smaller nor of lower kind than either type1 or type2. See type promotion
[documentation](../tensor_attributes.html#type-promotion-doc) for more information on the type
promotion logic.

Parameters:

- **type1** ([`torch.dtype`](../tensor_attributes.html#torch.dtype)) -
- **type2** ([`torch.dtype`](../tensor_attributes.html#torch.dtype)) -

Example:

```
>>> torch.promote_types(torch.int32, torch.float32)
torch.float32
>>> torch.promote_types(torch.uint8, torch.long)
torch.long
```