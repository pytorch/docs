# torch.cuda.graphs.graph_destroy_hooks_active

torch.cuda.graphs.graph_destroy_hooks_active()[[source]](https://github.com/pytorch/pytorch/blob/2e3c34c8bd8296fe6b14c14ec67f82e8af85507e/torch/cuda/graphs.py#L209)

True when any graph-destroy hook is registered - the gate a CUDAGraph checks before
arming its destroy callback.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)