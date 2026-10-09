# torch.cuda.graphs.register_graph_destroy_hook

torch.cuda.graphs.register_graph_destroy_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/cuda/graphs.py#L267)

Register `fn(graph_ids)` to run when a CUDA graph is destroyed. Returns a handle whose
`remove()` unregisters it.

Return type:

RemovableHandle