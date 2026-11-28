# torch.cuda.graphs.register_graph_capture_end_hook

torch.cuda.graphs.register_graph_capture_end_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/cuda/graphs.py#L223)

Register a hook run with each CUDA graph when its capture ends, while the captured
`cudaGraph_t` is still live (see [`CUDAGraph.register_capture_end_hook()`](torch.cuda.graphs.CUDAGraph.html#torch.cuda.graphs.CUDAGraph.register_capture_end_hook)). Returns a
RemovableHandle; call `.remove()` to unregister.

Return type:

RemovableHandle