# torch.cuda.graphs.run_graph_destroy_hooks

torch.cuda.graphs.run_graph_destroy_hooks(*exec_graph_ids*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/cuda/graphs.py#L215)

Invoke every registered hook with the destroyed exec graph ids, swallowing per-hook
errors so one failure does not abort the rest (matching the destroy-callback fire
semantics). The single entry point a graph's destroy callback calls.