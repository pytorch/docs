# torch.fx.experimental.proxy_tensor.get_proxy_mode

torch.fx.experimental.proxy_tensor.get_proxy_mode()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/fx/experimental/proxy_tensor.py#L3446)

Current the currently active proxy tracing mode, or None if
we are not currently tracing. This includes pre-dispatch proxy
tracing.

Return type:

*ProxyTorchDispatchMode* | None