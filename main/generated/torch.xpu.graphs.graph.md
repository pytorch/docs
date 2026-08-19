# graph

*class*torch.xpu.graphs.graph(*xpu_graph*, *pool=None*, *stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/3af07571b9d7402fd74352d079e6ff5fa307ec5f/torch/xpu/graphs.py#L150)

Context-manager that captures XPU work into a [`torch.xpu.XPUGraph`](torch.xpu.XPUGraph.html#torch.xpu.XPUGraph) object for later replay.

Parameters:

- **xpu_graph** ([*torch.xpu.XPUGraph*](torch.xpu.XPUGraph.html#torch.xpu.XPUGraph)) - Graph object used for capture.
- **pool** (*optional*) - Opaque token (returned by a call to [`graph_pool_handle()`](torch.xpu.graph_pool_handle.html#torch.xpu.graph_pool_handle) or
[`other_Graph_instance.pool()`](torch.xpu.XPUGraph.html#torch.xpu.XPUGraph.pool)) hinting this graph's capture
may share memory from the specified pool.
- **stream** ([*torch.xpu.Stream*](torch.xpu.Stream_class.html#torch.xpu.Stream)*,**optional*) - If supplied, will be set as the current stream in the context.
If not supplied, `graph` sets its own internal side stream as the current stream in the context.

Note

For effective memory sharing, if you pass a `pool` used by a previous capture and the previous capture
used an explicit `stream` argument, you should pass the same `stream` argument to this capture.