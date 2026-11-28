# torch.cuda.graphs.register_graph_instantiate_hook

torch.cuda.graphs.register_graph_instantiate_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/cuda/graphs.py#L232)

Register a hook run with each CUDA graph right after it is instantiated. Returns a
RemovableHandle; call `.remove()` to unregister.

Return type:

RemovableHandle