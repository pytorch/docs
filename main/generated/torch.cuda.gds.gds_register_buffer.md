# torch.cuda.gds.gds_register_buffer

torch.cuda.gds.gds_register_buffer(*s*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/gds.py#L63)

Registers a storage on a CUDA device as a cufile buffer.

Example:

```
>>> src = torch.randn(1024, device="cuda")
>>> s = src.untyped_storage()
>>> gds_register_buffer(s)
```

Parameters:

**s** (*Storage*) - Buffer to register.