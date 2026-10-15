# torch.cuda.gds.gds_deregister_buffer

torch.cuda.gds.gds_deregister_buffer(*s*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/cuda/gds.py#L83)

Deregisters a previously registered GDS buffer.

This is a wrapper around `cuFileBufDeregister` (CUDA) / `hipFileBufDeregister` (ROCm).

Example:

```
>>> src = torch.randn(1024, device="cuda")
>>> s = src.untyped_storage()
>>> gds_register_buffer(s)
>>> gds_deregister_buffer(s)
```

Parameters:

**s** (*Storage*) - Buffer to register.