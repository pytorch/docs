# torch.cuda.graphs.register_graph_capture_start_hook

torch.cuda.graphs.register_graph_capture_start_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/cuda/graphs.py#L206)

Register a hook run with each CUDA graph as its capture begins. Returns a
RemovableHandle; call `.remove()` to unregister.

Warning

The hook runs with capture already live on the current stream, so it must not issue
CUDA work: anything it launches is captured into the graph, and under the default
`"global"` capture error mode an unsafe call (e.g. an allocation) raises. Querying
capture state is fine. Do preparation that needs CUDA before the capture instead.

Return type:

RemovableHandle