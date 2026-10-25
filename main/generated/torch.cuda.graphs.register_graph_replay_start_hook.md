# torch.cuda.graphs.register_graph_replay_start_hook

torch.cuda.graphs.register_graph_replay_start_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/c9b5004c45376c912422325d032b2d74b4828d5c/torch/cuda/graphs.py#L238)

Register a hook run with each CUDA graph at the start of every replay, just before it
is launched. Returns a RemovableHandle; call `.remove()` to unregister.

Note

Replay is the hot path and this fires for EVERY graph on EVERY replay - keep it
cheap. With nothing registered the cost is a single dict emptiness check.

Return type:

RemovableHandle