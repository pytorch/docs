# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/bdfbe0c16b37fa7a4c09348321cabd906cb4019a/torch/fx/experimental/proxy_tensor.py#L878)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]