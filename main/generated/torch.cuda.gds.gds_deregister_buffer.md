# torch.cuda.gds.gds_deregister_buffer

torch.cuda.gds.gds_deregister_buffer(*s*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/gds.py#L83)

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