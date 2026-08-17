# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/99fcf9fd884002c14d4c19cce5dfe2469ba5a7fc/torch/fx/experimental/proxy_tensor.py#L847)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]