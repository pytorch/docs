# torch.cuda.graphs.graph_destroy_hooks_active

torch.cuda.graphs.graph_destroy_hooks_active()[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/cuda/graphs.py#L209)

True when any graph-destroy hook is registered - the gate a CUDAGraph checks before
arming its destroy callback.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)