# torch.cuda.gds.gds_register_buffer

torch.cuda.gds.gds_register_buffer(*s*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/cuda/gds.py#L65)

Registers a storage on a CUDA device as a GDS buffer.

This is a wrapper around `cuFileBufRegister` (CUDA) / `hipFileBufRegister` (ROCm).

Example:

```
>>> src = torch.randn(1024, device="cuda")
>>> s = src.untyped_storage()
>>> gds_register_buffer(s)
```

Parameters:

**s** (*Storage*) - Buffer to register.