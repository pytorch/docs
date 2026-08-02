# torch.cuda.graphs.run_graph_instantiate_hooks

torch.cuda.graphs.run_graph_instantiate_hooks(*torch_cuda_graph*)[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/cuda/graphs.py#L183)

Run every registered instantiate hook with the graph. Errors are swallowed so one
consumer cannot break instantiate() for another.