# torch.cuda.graphs.register_graph_destroy_hook

torch.cuda.graphs.register_graph_destroy_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/cuda/graphs.py#L268)

Register `fn(exec_ids)` to run when a CUDA graph is destroyed. Returns a handle whose
`remove()` unregisters it.

Return type:

RemovableHandle