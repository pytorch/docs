# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/7a37a01092627acd59ddfcb9cefe5a578f5f6996/torch/fx/experimental/proxy_tensor.py#L836)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]