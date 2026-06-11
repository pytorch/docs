# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/fx/experimental/proxy_tensor.py#L818)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]