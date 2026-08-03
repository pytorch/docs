# torch.cuda.graphs.register_graph_instantiate_hook

torch.cuda.graphs.register_graph_instantiate_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/cuda/graphs.py#L171)

Register a hook run with each CUDA graph right after it is instantiated. Returns a
RemovableHandle; call `.remove()` to unregister.

Return type:

RemovableHandle