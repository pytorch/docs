# torch.result_type

torch.result_type(*tensor1*, *tensor2*) → [dtype](../tensor_attributes.html#torch.dtype)

Returns the [`torch.dtype`](../tensor_attributes.html#torch.dtype) that would result from performing an arithmetic
operation on the provided input tensors. See type promotion [documentation](../tensor_attributes.html#type-promotion-doc)
for more information on the type promotion logic.

Parameters:

- **tensor1** ([*Tensor*](../tensors.html#torch.Tensor)*or**Number*) - an input tensor or number
- **tensor2** ([*Tensor*](../tensors.html#torch.Tensor)*or**Number*) - an input tensor or number

Example:

```
>>> torch.result_type(torch.tensor([1, 2], dtype=torch.int), 1.0)
torch.float32
>>> torch.result_type(torch.tensor([1, 2], dtype=torch.uint8), torch.tensor(1))
torch.uint8
```