# torch.cuda.graphs.register_graph_replay_end_hook

torch.cuda.graphs.register_graph_replay_end_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/cuda/graphs.py#L251)

Register a hook run with each CUDA graph at the end of every replay, once the replay is
*enqueued* (the launch is asynchronous, so the GPU work has not completed). Fires even if
the launch raised, so a start hook is always balanced by an end. Returns a RemovableHandle;
call `.remove()` to unregister. See the hot-path note on
[`register_graph_replay_start_hook()`](torch.cuda.graphs.register_graph_replay_start_hook.html#torch.cuda.graphs.register_graph_replay_start_hook).

Return type:

RemovableHandle