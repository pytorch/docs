# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/fx/experimental/proxy_tensor.py#L801)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]