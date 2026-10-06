# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/fx/experimental/proxy_tensor.py#L848)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]