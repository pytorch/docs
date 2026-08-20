# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/fx/experimental/proxy_tensor.py#L847)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]