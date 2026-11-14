# torch.cuda.gds.gds_deregister_buffer

torch.cuda.gds.gds_deregister_buffer(*s*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/cuda/gds.py#L93)

Deregisters a previously registered GDS buffer.

This is a wrapper around `cuFileBufDeregister` (CUDA) / `hipFileBufDeregister` (ROCm).
It first synchronizes the storage's device, so that any
[`GdsFile.load_storage_async()`](torch.cuda.gds.GdsFile.html#torch.cuda.gds.GdsFile.load_storage_async) or [`GdsFile.save_storage_async()`](torch.cuda.gds.GdsFile.html#torch.cuda.gds.GdsFile.save_storage_async)
still pending on the buffer has run.

Example:

```
>>> src = torch.randn(1024, device="cuda")
>>> s = src.untyped_storage()
>>> gds_register_buffer(s)
>>> gds_deregister_buffer(s)
```

Parameters:

**s** (*Storage*) - Buffer to register.