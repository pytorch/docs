# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/fx/experimental/proxy_tensor.py#L847)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]