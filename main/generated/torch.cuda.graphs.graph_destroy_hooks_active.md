# torch.cuda.graphs.graph_destroy_hooks_active

torch.cuda.graphs.graph_destroy_hooks_active()[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/cuda/graphs.py#L209)

True when any graph-destroy hook is registered - the gate a CUDAGraph checks before
arming its destroy callback.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)