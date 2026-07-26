# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/fx/experimental/proxy_tensor.py#L838)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]