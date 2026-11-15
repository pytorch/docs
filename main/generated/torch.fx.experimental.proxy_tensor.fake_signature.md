# torch.fx.experimental.proxy_tensor.fake_signature

torch.fx.experimental.proxy_tensor.fake_signature(*fn*, *nargs*)[[source]](https://github.com/pytorch/pytorch/blob/c79633996ebc2114482ae5a4ff3cb409d79a8a9c/torch/fx/experimental/proxy_tensor.py#L175)

FX gets confused by varargs, de-confuse it

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *R*]