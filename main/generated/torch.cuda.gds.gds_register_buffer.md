# torch.cuda.gds.gds_register_buffer

torch.cuda.gds.gds_register_buffer(*s*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/cuda/gds.py#L53)

Registers a storage on a CUDA device as a cufile buffer.

Example:

```
>>> src = torch.randn(1024, device="cuda")
>>> s = src.untyped_storage()
>>> gds_register_buffer(s)
```

Parameters:

**s** (*Storage*) - Buffer to register.