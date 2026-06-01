# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/5cd392bfe432d57e7beb9ab67037ddc0fcc01205/torch/fx/experimental/proxy_tensor.py#L796)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]