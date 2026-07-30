# torch.cuda.graphs.run_graph_instantiate_hooks

torch.cuda.graphs.run_graph_instantiate_hooks(*torch_cuda_graph*)[[source]](https://github.com/pytorch/pytorch/blob/9179f2014ca7f941551131fc2315cfcf9e206bd3/torch/cuda/graphs.py#L183)

Run every registered instantiate hook with the graph. Errors are swallowed so one
consumer cannot break instantiate() for another.