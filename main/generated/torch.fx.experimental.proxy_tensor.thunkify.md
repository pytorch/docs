# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/fx/experimental/proxy_tensor.py#L796)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]