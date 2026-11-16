# torch.cuda.gds.gds_register_buffer

torch.cuda.gds.gds_register_buffer(*s*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/cuda/gds.py#L75)

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