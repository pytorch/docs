# torch.cuda.gds.gds_register_buffer

torch.cuda.gds.gds_register_buffer(*s*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/cuda/gds.py#L53)

Registers a storage on a CUDA device as a cufile buffer.

Example:

```
>>> src = torch.randn(1024, device="cuda")
>>> s = src.untyped_storage()
>>> gds_register_buffer(s)
```

Parameters:

**s** (*Storage*) - Buffer to register.