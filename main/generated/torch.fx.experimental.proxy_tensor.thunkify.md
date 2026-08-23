# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/fx/experimental/proxy_tensor.py#L847)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]