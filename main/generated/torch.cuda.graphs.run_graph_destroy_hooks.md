# torch.cuda.graphs.run_graph_destroy_hooks

torch.cuda.graphs.run_graph_destroy_hooks(*exec_graph_ids*)[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/cuda/graphs.py#L215)

Invoke every registered hook with the destroyed exec graph ids, swallowing per-hook
errors so one failure does not abort the rest (matching the destroy-callback fire
semantics). The single entry point a graph's destroy callback calls.