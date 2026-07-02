# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/fx/experimental/proxy_tensor.py#L829)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]