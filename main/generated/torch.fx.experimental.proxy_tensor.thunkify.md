# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/5f228673c58f6d36691c0cbc5c677fdf0c349372/torch/fx/experimental/proxy_tensor.py#L891)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]