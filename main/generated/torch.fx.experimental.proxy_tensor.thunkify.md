# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/fx/experimental/proxy_tensor.py#L801)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]