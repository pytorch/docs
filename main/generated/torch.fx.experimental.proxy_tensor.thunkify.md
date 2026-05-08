# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/fx/experimental/proxy_tensor.py#L796)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]