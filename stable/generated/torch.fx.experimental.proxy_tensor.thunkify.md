# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/fx/experimental/proxy_tensor.py#L800)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]