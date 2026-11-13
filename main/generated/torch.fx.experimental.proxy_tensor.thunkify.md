# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/b896199bee9ca0e125f6ec366a265418a8f3290e/torch/fx/experimental/proxy_tensor.py#L878)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]