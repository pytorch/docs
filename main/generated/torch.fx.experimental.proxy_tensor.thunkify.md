# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/fx/experimental/proxy_tensor.py#L878)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]