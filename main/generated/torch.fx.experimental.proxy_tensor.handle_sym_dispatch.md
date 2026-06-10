# torch.fx.experimental.proxy_tensor.handle_sym_dispatch

torch.fx.experimental.proxy_tensor.handle_sym_dispatch(*func*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/fx/experimental/proxy_tensor.py#L3090)

Call into the currently active proxy tracing mode to do a
SymInt/SymFloat/SymBool dispatch trace on a function that operates on
these arguments.

Return type:

*R*