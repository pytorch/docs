# CUDAGraph

*class*torch.cuda.graphs.CUDAGraph(*keep_graph=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L77)

Wrapper around a CUDA graph.

Parameters:

**keep_graph** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `keep_graph=False`, the
cudaGraphExec_t will be instantiated on GPU at the end of
`capture_end` and the underlying cudaGraph_t will be
destroyed. Users who want to query or otherwise modify the
underlying cudaGraph_t before instantiation can set
`keep_graph=True` and access it via `raw_cuda_graph` after
`capture_end`. Note that the cudaGraphExec_t will not be
instantiated at the end of `capture_end` in this
case. Instead, it will be instantiated via an explicit called
to `instantiate` or automatically on the first call to
`replay` if `instantiate` was not already called. Calling
`instantiate` manually before `replay` is recommended to
prevent increased latency on the first call to `replay`. It
is allowed to modify the raw cudaGraph_t after first calling
`instantiate`, but the user must call `instantiate` again
manually to make sure the instantiated graph has these
changes. Pytorch has no means of tracking these changes.

Return type:

Self

Warning

This API is in beta and may change in future releases.

capture_begin(*pool=None*, *capture_error_mode='global'*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L107)

Begin capturing CUDA work on the current stream.

Typically, you shouldn't call `capture_begin` yourself.
Use [`graph`](torch.cuda.graph.html#torch.cuda.graph) or [`make_graphed_callables()`](torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables),
which call `capture_begin` internally.

Parameters:

- **pool** (*optional*) - Token (returned by [`graph_pool_handle()`](torch.cuda.graph_pool_handle.html#torch.cuda.graph_pool_handle) or
[`other_Graph_instance.pool()`](torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.pool)) that hints this graph may share memory
with the indicated pool. See [Graph memory management](../notes/cuda.html#graph-memory-management).
- **capture_error_mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - specifies the cudaStreamCaptureMode for the graph capture stream.
Can be "global", "thread_local" or "relaxed". During cuda graph capture, some actions, such as cudaMalloc,
may be unsafe. "global" will error on actions in other threads, "thread_local" will only error for
actions in the current thread, and "relaxed" will not error on these actions. Do NOT change this setting
unless you're familiar with [cudaStreamCaptureMode](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html#group__CUDART__STREAM_1g9d0535d93a214cbf126835257b16ba85)

capture_end()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L128)

End CUDA graph capture on the current stream.

After `capture_end`, `replay` may be called on this instance.

Typically, you shouldn't call `capture_end` yourself.
Use [`graph`](torch.cuda.graph.html#torch.cuda.graph) or [`make_graphed_callables()`](torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables),
which call `capture_end` internally.

debug_dump(*debug_path*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L168)

Parameters:

**debug_path** (*required*) - Path to dump the graph to.

Calls a debugging function to dump the graph if the debugging is
enabled via CUDAGraph.enable_debug_mode()

enable_debug_mode()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L164)

Enable debugging mode for CUDAGraph.debug_dump.

get_graph_data()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L192)

Return a dictionary describing the graph's topology and node metadata.

`keep_graph` must be True. The graph must have been instantiated
(via `instantiate()`) before calling this method.
Requires the `cuda.bindings` package.

Returns a dictionary with structure:

```
{
 "exec_graph_id": int,
 "nodes": [
 {
 "index": int,
 "node_type": str,
 "tools_id": int,
 "graph_id": int,
 "node_id": int,
 "kernel_name": str or None,
 "dependencies": [int, ...],
 "dependents": [int, ...],
 },
 ...,
 ],
}
```

Each node's `graph_id` is remapped to the exec graph id so that
`tools_id` values match those reported by CUPTI-based profilers.
`dependencies` and `dependents` are lists of node indices within
the `nodes` list.

This structure is useful for inspecting a profiler trace and
establishing whether a particular dependency observed in the profile
is a true dependency (encoded in the graph) or a fake dependency
caused by mapping of independent streams to the same hardware
channel.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)

instantiate()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L139)

Instantiate the CUDA graph. Will be called by
`capture_end` if `keep_graph=False`, or by `replay` if
`keep_graph=True` and `instantiate` has not already been
explicitly called. Does not destroy the cudaGraph_t returned
by `raw_cuda_graph`.

pool()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L156)

Return an opaque token representing the id of this graph's memory pool.

This id can optionally be passed to another graph's `capture_begin`,
which hints the other graph may share the same memory pool.

Return type:

_POOL_HANDLE

raw_cuda_graph()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L178)

Returns the underlying cudaGraph_t. `keep_graph` must be True.

See the following for APIs for how to manipulate this object: [Graph Management](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__GRAPH.html) and [cuda-python Graph Management bindings](https://nvidia.github.io/cuda-python/cuda-bindings/latest/module/runtime.html#graph-management)

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

raw_cuda_graph_exec()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L185)

Returns the underlying cudaGraphExec_t. `instantiate` must have been called if `keep_graph` is True, or `capture_end` must have been called if `keep_graph` is False. If you call `instantiate()` after `raw_cuda_graph_exec()`, the previously returned cudaGraphExec_t will be destroyed. It is your responsibility not to use this object after destruction.

See the following for APIs for how to manipulate this object: [Graph Execution](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__GRAPH__EXEC.html) and [cuda-python Graph Execution bindings](https://nvidia.github.io/cuda-python/cuda-bindings/latest/module/runtime.html#graph-execution)

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

replay()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L148)

Replay the CUDA work captured by this graph.

reset()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/cuda/graphs.py#L152)

Delete the graph currently held by this instance.