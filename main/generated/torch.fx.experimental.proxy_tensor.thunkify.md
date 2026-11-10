# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/fx/experimental/proxy_tensor.py#L878)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]