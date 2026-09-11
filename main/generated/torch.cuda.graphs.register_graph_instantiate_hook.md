# torch.cuda.graphs.register_graph_instantiate_hook

torch.cuda.graphs.register_graph_instantiate_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/cuda/graphs.py#L230)

Register a hook run with each CUDA graph right after it is instantiated. Returns a
RemovableHandle; call `.remove()` to unregister.

Return type:

RemovableHandle