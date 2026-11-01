# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/6728ae647ab077842210f24d515b54df7709e144/torch/fx/experimental/proxy_tensor.py#L850)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]