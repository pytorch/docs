# torch.fx.experimental.proxy_tensor.handle_sym_dispatch

torch.fx.experimental.proxy_tensor.handle_sym_dispatch(*func*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/fx/experimental/proxy_tensor.py#L3461)

Call into the currently active proxy tracing mode to do a
SymInt/SymFloat/SymBool dispatch trace on a function that operates on
these arguments.

Return type:

*R*