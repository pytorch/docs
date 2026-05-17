# XPUGraph

*class*torch.xpu.XPUGraph(*keep_graph=False*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/xpu/graphs.py#L53)

Wrapper around a XPU graph.

Parameters:

**keep_graph** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `keep_graph=False`, the
executable command graph will be instantiated on GPU at the end of
`capture_end` and the underlying modifiable command graph will be
destroyed. Note that the executable command graph will not be
instantiated at the end of `capture_end` in this
case. Instead, it will be instantiated via an explicit called
to `instantiate` or automatically on the first call to
`replay` if `instantiate` was not already called. Calling
`instantiate` manually before `replay` is recommended to
prevent increased latency on the first call to `replay`.

Return type:

Self

capture_begin(*pool=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/xpu/graphs.py#L73)

Begin capturing XPU work on the current xpu stream.

Typically, you shouldn't call `capture_begin` yourself.
Use [`graph`](torch.xpu.graph.html#torch.xpu.graph), which call `capture_begin` internally.

Parameters:

**pool** (*optional*) - Token (returned by [`graph_pool_handle()`](torch.xpu.graph_pool_handle.html#torch.xpu.graph_pool_handle) or
`other_Graph_instance.pool()`) that hints this graph may share memory
with the indicated pool.

capture_end()[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/xpu/graphs.py#L86)

End XPU graph capture on the current stream.

After `capture_end`, `replay` may be called on this instance.

Typically, you shouldn't call `capture_end` yourself.
Use [`graph`](torch.xpu.graph.html#torch.xpu.graph), which call `capture_end` internally.

debug_dump(*debug_path*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/xpu/graphs.py#L125)

Parameters:

**debug_path** (*required*) - Path to dump the graph to.

Calls a debugging function to dump the graph if the debugging is
enabled via XPUGraph.enable_debug_mode()

enable_debug_mode()[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/xpu/graphs.py#L121)

Enable debugging mode for XPUGraph.debug_dump.

instantiate()[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/xpu/graphs.py#L96)

Instantiate the XPU graph. Will be called by
`capture_end` if `keep_graph=False`, or by `replay` if
`keep_graph=True` and `instantiate` has not already been
explicitly called. Does not destroy the xpu modify command graph returned
by `raw_xpu_graph`.

pool()[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/xpu/graphs.py#L113)

Return an opaque token representing the id of this graph's memory pool.

This id can optionally be passed to another graph's `capture_begin`,
which hints the other graph may share the same memory pool.

Return type:

_POOL_HANDLE

raw_xpu_graph()[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/xpu/graphs.py#L135)

Returns the underlying xpuGraph_t. `keep_graph` must be True.

XPU doesn't provide APIs to manipulate this object.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

raw_xpu_graph_exec()[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/xpu/graphs.py#L142)

Returns the underlying xpuGraphExec_t. `instantiate` must have been called if `keep_graph` is True, or `capture_end` must have been called if `keep_graph` is False. If you call `instantiate()` after `raw_xpu_graph_exec()`, the previously returned xpuGraphExec_t will be destroyed. It is your responsibility not to use this object after destruction.

XPU doesn't provide APIs to manipulate this object.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

replay()[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/xpu/graphs.py#L105)

Replay the XPU work captured by this graph.

reset()[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/xpu/graphs.py#L109)

Delete the graph currently held by this instance.