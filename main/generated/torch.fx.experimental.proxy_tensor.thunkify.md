# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/efbc87071fdf61bd50d5dc3b315b65bd452c401d/torch/fx/experimental/proxy_tensor.py#L891)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]