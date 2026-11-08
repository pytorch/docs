# torch.fx.experimental.proxy_tensor.get_proxy_mode

torch.fx.experimental.proxy_tensor.get_proxy_mode()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/experimental/proxy_tensor.py#L3583)

Current the currently active proxy tracing mode, or None if
we are not currently tracing. This includes pre-dispatch proxy
tracing.

Return type:

*ProxyTorchDispatchMode* | None