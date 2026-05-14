# torch.cuda.gds.gds_deregister_buffer

torch.cuda.gds.gds_deregister_buffer(*s*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/gds.py#L69)

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