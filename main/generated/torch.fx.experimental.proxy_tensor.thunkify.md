# torch.fx.experimental.proxy_tensor.thunkify

torch.fx.experimental.proxy_tensor.thunkify(*tracer*, *f*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/fx/experimental/proxy_tensor.py#L796)

Delays computation of f until it's called again
Also caches the result

Return type:

*Thunk*[*R*]