# torch.cuda.graphs.run_graph_instantiate_hooks

torch.cuda.graphs.run_graph_instantiate_hooks(*torch_cuda_graph*)[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/cuda/graphs.py#L183)

Run every registered instantiate hook with the graph. Errors are swallowed so one
consumer cannot break instantiate() for another.