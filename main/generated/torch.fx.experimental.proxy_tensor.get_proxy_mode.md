# torch.fx.experimental.proxy_tensor.get_proxy_mode

torch.fx.experimental.proxy_tensor.get_proxy_mode()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/fx/experimental/proxy_tensor.py#L3047)

Current the currently active proxy tracing mode, or None if
we are not currently tracing. This includes pre-dispatch proxy
tracing.

Return type:

*ProxyTorchDispatchMode* | None