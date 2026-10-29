# torch.fx.experimental.proxy_tensor.fake_signature

torch.fx.experimental.proxy_tensor.fake_signature(*fn*, *nargs*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/fx/experimental/proxy_tensor.py#L169)

FX gets confused by varargs, de-confuse it

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *R*]