# torch.cuda.graphs.register_graph_capture_end_hook

torch.cuda.graphs.register_graph_capture_end_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/cuda/graphs.py#L221)

Register a hook run with each CUDA graph when its capture ends, while the captured
`cudaGraph_t` is still live (see [`CUDAGraph.register_capture_end_hook()`](torch.cuda.graphs.CUDAGraph.html#torch.cuda.graphs.CUDAGraph.register_capture_end_hook)). Returns a
RemovableHandle; call `.remove()` to unregister.

Return type:

RemovableHandle