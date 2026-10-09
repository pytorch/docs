# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/fx/experimental/proxy_tensor.py#L848)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]