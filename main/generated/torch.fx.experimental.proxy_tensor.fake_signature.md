# torch.fx.experimental.proxy_tensor.fake_signature

torch.fx.experimental.proxy_tensor.fake_signature(*fn*, *nargs*)[[source]](https://github.com/pytorch/pytorch/blob/69bbaeafe0b3f1e423be17b25ca11b149845b521/torch/fx/experimental/proxy_tensor.py#L154)

FX gets confused by varargs, de-confuse it

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *R*]