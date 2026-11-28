# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/fx/experimental/proxy_tensor.py#L891)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]