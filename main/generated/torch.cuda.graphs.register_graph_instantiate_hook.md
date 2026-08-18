# torch.cuda.graphs.register_graph_instantiate_hook

torch.cuda.graphs.register_graph_instantiate_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/cuda/graphs.py#L230)

Register a hook run with each CUDA graph right after it is instantiated. Returns a
RemovableHandle; call `.remove()` to unregister.

Return type:

RemovableHandle