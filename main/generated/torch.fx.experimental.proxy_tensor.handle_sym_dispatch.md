# torch.fx.experimental.proxy_tensor.handle_sym_dispatch

torch.fx.experimental.proxy_tensor.handle_sym_dispatch(*func*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/fx/experimental/proxy_tensor.py#L3413)

Call into the currently active proxy tracing mode to do a
SymInt/SymFloat/SymBool dispatch trace on a function that operates on
these arguments.

Return type:

*R*