# torch.cuda.graphs.register_graph_destroy_hook

torch.cuda.graphs.register_graph_destroy_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/cuda/graphs.py#L268)

Register `fn(exec_ids)` to run when a CUDA graph is destroyed. Returns a handle whose
`remove()` unregisters it.

Return type:

RemovableHandle