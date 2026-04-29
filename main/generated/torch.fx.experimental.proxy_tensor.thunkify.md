# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/fx/experimental/proxy_tensor.py#L801)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]