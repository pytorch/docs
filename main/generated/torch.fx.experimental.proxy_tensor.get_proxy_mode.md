# torch.fx.experimental.proxy_tensor.get_proxy_mode

torch.fx.experimental.proxy_tensor.get_proxy_mode()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/fx/experimental/proxy_tensor.py#L3398)

Current the currently active proxy tracing mode, or None if
we are not currently tracing. This includes pre-dispatch proxy
tracing.

Return type:

*ProxyTorchDispatchMode* | None