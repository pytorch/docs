# torch.get_default_dtype

torch.get_default_dtype() → [torch.dtype](../tensor_attributes.html#torch.dtype)

Get the current default floating point [`torch.dtype`](../tensor_attributes.html#torch.dtype).

Example:

```
>>> torch.get_default_dtype() # initial default for floating point is torch.float32
torch.float32
>>> torch.set_default_dtype(torch.float64)
>>> torch.get_default_dtype() # default is now changed to torch.float64
torch.float64
```