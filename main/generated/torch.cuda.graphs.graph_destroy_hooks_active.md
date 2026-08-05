# torch.cuda.graphs.graph_destroy_hooks_active

torch.cuda.graphs.graph_destroy_hooks_active()[[source]](https://github.com/pytorch/pytorch/blob/e3b3670d208b9e770a7ca36a3fed1ea0f052f799/torch/cuda/graphs.py#L210)

True when any graph-destroy hook is registered - the gate a CUDAGraph checks before
arming its destroy callback.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)