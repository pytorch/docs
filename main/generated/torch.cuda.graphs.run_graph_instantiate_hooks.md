# torch.cuda.graphs.run_graph_instantiate_hooks

torch.cuda.graphs.run_graph_instantiate_hooks(*torch_cuda_graph*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/cuda/graphs.py#L185)

Run every registered instantiate hook with the graph. Errors are swallowed so one
consumer cannot break instantiate() for another.