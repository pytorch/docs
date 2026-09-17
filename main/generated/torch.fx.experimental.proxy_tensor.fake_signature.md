# torch.fx.experimental.proxy_tensor.fake_signature

torch.fx.experimental.proxy_tensor.fake_signature(*fn*, *nargs*)[[source]](https://github.com/pytorch/pytorch/blob/65c295bfa29161891e39b83fac63c4f5417ffdc2/torch/fx/experimental/proxy_tensor.py#L168)

FX gets confused by varargs, de-confuse it

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *R*]