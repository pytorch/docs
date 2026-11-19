# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/a4a15a72064ca010a723eae7c73835fe206f8de6/torch/fx/experimental/proxy_tensor.py#L882)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]