# torch.fx.experimental.proxy_tensor.get_proxy_mode

torch.fx.experimental.proxy_tensor.get_proxy_mode()[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/fx/experimental/proxy_tensor.py#L3566)

Current the currently active proxy tracing mode, or None if
we are not currently tracing. This includes pre-dispatch proxy
tracing.

Return type:

*ProxyTorchDispatchMode* | None