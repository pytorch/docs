# torch.cuda.gds.gds_deregister_buffer

torch.cuda.gds.gds_deregister_buffer(*s*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/cuda/gds.py#L79)

Deregisters a previously registered storage on a CUDA device as a cufile buffer.

Example:

```
>>> src = torch.randn(1024, device="cuda")
>>> s = src.untyped_storage()
>>> gds_register_buffer(s)
>>> gds_deregister_buffer(s)
```

Parameters:

**s** (*Storage*) - Buffer to register.