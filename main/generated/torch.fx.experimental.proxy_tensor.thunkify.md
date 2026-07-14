# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/fx/experimental/proxy_tensor.py#L836)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]