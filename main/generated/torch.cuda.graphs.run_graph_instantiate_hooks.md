# torch.cuda.graphs.run_graph_instantiate_hooks

torch.cuda.graphs.run_graph_instantiate_hooks(*torch_cuda_graph*)[[source]](https://github.com/pytorch/pytorch/blob/e3b3670d208b9e770a7ca36a3fed1ea0f052f799/torch/cuda/graphs.py#L184)

Run every registered instantiate hook with the graph. Errors are swallowed so one
consumer cannot break instantiate() for another.