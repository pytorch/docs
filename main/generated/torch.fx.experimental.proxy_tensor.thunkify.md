# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/94de2113ebf2891e498dd58ed1a16fedac39b5c6/torch/fx/experimental/proxy_tensor.py#L838)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]