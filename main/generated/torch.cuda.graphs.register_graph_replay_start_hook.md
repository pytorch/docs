# torch.cuda.graphs.register_graph_replay_start_hook

torch.cuda.graphs.register_graph_replay_start_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/cuda/graphs.py#L238)

Register a hook run with each CUDA graph at the start of every replay, just before it
is launched. Returns a RemovableHandle; call `.remove()` to unregister.

Note

Replay is the hot path and this fires for EVERY graph on EVERY replay - keep it
cheap. With nothing registered the cost is a single dict emptiness check.

Return type:

RemovableHandle