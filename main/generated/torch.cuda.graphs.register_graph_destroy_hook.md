# torch.cuda.graphs.register_graph_destroy_hook

torch.cuda.graphs.register_graph_destroy_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/cuda/graphs.py#L269)

Register `fn(graph_ids)` to run when a CUDA graph is destroyed. Returns a handle whose
`remove()` unregisters it.

Return type:

RemovableHandle