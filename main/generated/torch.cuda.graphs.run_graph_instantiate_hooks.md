# torch.cuda.graphs.run_graph_instantiate_hooks

torch.cuda.graphs.run_graph_instantiate_hooks(*torch_cuda_graph*)[[source]](https://github.com/pytorch/pytorch/blob/2e3c34c8bd8296fe6b14c14ec67f82e8af85507e/torch/cuda/graphs.py#L183)

Run every registered instantiate hook with the graph. Errors are swallowed so one
consumer cannot break instantiate() for another.