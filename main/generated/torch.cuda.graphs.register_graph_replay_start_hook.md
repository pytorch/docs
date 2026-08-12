# torch.cuda.graphs.register_graph_replay_start_hook

torch.cuda.graphs.register_graph_replay_start_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/cuda/graphs.py#L238)

Register a hook run with each CUDA graph at the start of every replay, just before it
is launched. Returns a RemovableHandle; call `.remove()` to unregister.

Note

Replay is the hot path and this fires for EVERY graph on EVERY replay - keep it
cheap. With nothing registered the cost is a single dict emptiness check.

Return type:

RemovableHandle