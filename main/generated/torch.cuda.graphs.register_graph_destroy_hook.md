# torch.cuda.graphs.register_graph_destroy_hook

torch.cuda.graphs.register_graph_destroy_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/cuda/graphs.py#L267)

Register `fn(graph_ids)` to run when a CUDA graph is destroyed. Returns a handle whose
`remove()` unregisters it.

Return type:

RemovableHandle