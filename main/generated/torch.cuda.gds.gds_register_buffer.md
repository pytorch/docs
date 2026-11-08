# torch.cuda.gds.gds_register_buffer

torch.cuda.gds.gds_register_buffer(*s*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/cuda/gds.py#L75)

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