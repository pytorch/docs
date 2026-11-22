# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/65e101a3cc8242711ae1cb467ed6cde097135821/torch/fx/experimental/proxy_tensor.py#L891)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]