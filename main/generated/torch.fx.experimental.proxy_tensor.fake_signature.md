# torch.fx.experimental.proxy_tensor.fake_signature

torch.fx.experimental.proxy_tensor.fake_signature(*fn*, *nargs*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/fx/experimental/proxy_tensor.py#L154)

FX gets confused by varargs, de-confuse it

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *R*]