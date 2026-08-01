# torch.cuda.graphs.register_graph_instantiate_hook

torch.cuda.graphs.register_graph_instantiate_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/2e3c34c8bd8296fe6b14c14ec67f82e8af85507e/torch/cuda/graphs.py#L171)

Register a hook run with each CUDA graph right after it is instantiated. Returns a
RemovableHandle; call `.remove()` to unregister.

Return type:

RemovableHandle