# CUDAGraph

*class*torch.cuda.CUDAGraph(*keep_graph=False*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L296)

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
case. Instead, it will be instantiated via an explicit call
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

capture_begin(*pool=None*, *capture_error_mode='global'*, *check_input_liveness=False*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L576)

Begin capturing CUDA work on the current stream.

Typically, you shouldn't call `capture_begin` yourself.
Use [`graph`](torch.cuda.graph.html#torch.cuda.graph) or [`make_graphed_callables()`](torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables),
which call `capture_begin` internally.

Parameters:

- **pool** (*optional*) - Token (returned by [`graph_pool_handle()`](torch.cuda.graph_pool_handle.html#torch.cuda.graph_pool_handle) or
`other_Graph_instance.pool()`) or
`MemPool` that hints this graph may share memory
with the indicated pool. See [Graph memory management](../notes/cuda.html#graph-memory-management).
- **capture_error_mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - specifies the cudaStreamCaptureMode for the graph capture stream.
Can be "global", "thread_local" or "relaxed". During cuda graph capture, some actions, such as cudaMalloc,
may be unsafe. "global" will error on actions in other threads, "thread_local" will only error for
actions in the current thread, and "relaxed" will not error on these actions. Do NOT change this setting
unless you're familiar with [cudaStreamCaptureMode](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html#group__CUDART__STREAM_1g9d0535d93a214cbf126835257b16ba85)
- **check_input_liveness** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) -

If `True`, tracks external tensor inputs during graph capture and
raises an error if any are deallocated before replay. This helps debug "use after free" errors
where input tensors are garbage collected between capture and replay. Default: `False`.

Note

Custom CUDA kernels added outside PyTorch (e.g., via cuLaunchKernel or DLPack) are not
tracked by this mechanism.

capture_end()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L640)

End CUDA graph capture on the current stream.

After `capture_end`, `replay` may be called on this instance.

Typically, you shouldn't call `capture_end` yourself.
Use [`graph`](torch.cuda.graph.html#torch.cuda.graph) or [`make_graphed_callables()`](torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables),
which call `capture_end` internally.

capture_end_post()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L632)

Finalize a capture started by `capture_end_pre()`: destroy the
template when `keep_graph=False` (the graph must already be
instantiated; `capture_end()` and the context manager do so).

capture_end_pre()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L626)

End capture but do not finalize: leaves the captured `cudaGraph_t`
live (for both `keep_graph` modes) so it can be inspected before
`capture_end_post()` instantiates and/or destroys it.

debug_dump(*debug_path*, ***, *verbose=True*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L763)

Dump the captured graph to `debug_path` in Graphviz DOT format.

The graph's template must be live: `keep_graph=True` (or
`enable_debug_mode()`), or called from a capture-end hook. Requires
the `cuda.bindings` package.

Parameters:

- **debug_path** (*required*) - Path to dump the graph to.
- **verbose** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True` (default), use the most verbose DOT output.

enable_debug_mode()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L755)

Retain the captured graph (equivalent to `keep_graph=True`) so it
can be inspected, e.g. via `debug_dump()`. Kept for backward
compatibility.

get_graph_data()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L793)

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
 "event_ptr": int,
 "host_fn_addr": int,
 "host_fn_name": str or None,
 "dependencies": [int, ...],
 "dependents": [int, ...],
 },
 ...,
 ],
}
```

`event_ptr` is the `cudaEvent_t` handle (as an int) an event-record
or event-wait node records / waits on - these nodes produce no timed
CUPTI record, so matching a wait to the record that signals it is the
only way to reason about the cross-stream sync it encodes. It is `0`
for other node types.

`host_fn_addr` / `host_fn_name` are populated for host nodes (a CPU
callback run as a graph node): the callback address and a best-effort
demangled symbol name for it (`None` when it resolves to no exported
symbol). They are `0` / `None` for other node types.

Each node's `graph_id` is remapped to the exec graph id so that
`tools_id` values match those reported by CUPTI-based profilers.
`dependencies` and `dependents` are lists of node indices within
the `nodes` list.

This structure is useful for inspecting a profiler trace and
establishing whether a particular dependency observed in the profile
is a true dependency (encoded in the graph) or a fake dependency
caused by mapping of independent streams to the same hardware
channel.

Child-graph and conditional nodes are reported as nodes in their own
right, but this walk does not descend into their bodies (those are
separate `cudaGraph_t` objects), so the work inside them is absent
from `nodes` and a warning is issued. The ids that *are* reported
stay valid: the exec graph preserves top-level node ids.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)

instantiate()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L665)

Instantiate the CUDA graph. Will be called by
`capture_end` if `keep_graph=False`, or by `replay` if
`keep_graph=True` and `instantiate` has not already been
explicitly called. Does not destroy the cudaGraph_t returned
by `raw_cuda_graph`.

pool()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L737)

Return an opaque token representing the id of this graph's memory pool.

This id can optionally be passed to another graph's `capture_begin`,
which hints the other graph may share the same memory pool.

Return type:

_POOL_HANDLE

pools()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L745)

Return opaque tokens for all memory pools retained by this graph.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[_POOL_HANDLE]

raw_cuda_graph()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L776)

Returns the underlying cudaGraph_t. The template must be live: this
requires `keep_graph=True` (it persists after `capture_end`), or
access from within a capture-end hook (before the template is destroyed
for `keep_graph=False`).

See the following for APIs for how to manipulate this object: [Graph Management](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__GRAPH.html) and [cuda-python Graph Management bindings](https://nvidia.github.io/cuda-python/cuda-bindings/latest/module/runtime.html#graph-management)

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

raw_cuda_graph_exec()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L786)

Returns the underlying cudaGraphExec_t. `instantiate` must have been called if `keep_graph` is True, or `capture_end` must have been called if `keep_graph` is False. If you call `instantiate()` after `raw_cuda_graph_exec()`, the previously returned cudaGraphExec_t will be destroyed. It is your responsibility not to use this object after destruction.

See the following for APIs for how to manipulate this object: [Graph Execution](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__GRAPH__EXEC.html) and [cuda-python Graph Execution bindings](https://nvidia.github.io/cuda-python/cuda-bindings/latest/module/runtime.html#graph-execution)

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

register_capture_end_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L416)

Register `hook(graph)` to run when capture ends, after capture
completes but before the graph is finalized. The captured `cudaGraph_t`
is live (via `raw_cuda_graph()`) for both `keep_graph` modes. Hooks
fire in registration order. Returns a handle whose `remove()`
deregisters the hook.

Return type:

RemovableHandle

register_capture_start_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L398)

Register `hook(graph)` to run when capture begins on this graph, right
after capture is under way on the current stream. Hooks fire in registration
order. Returns a handle whose `remove()` deregisters the hook.

Warning

The hook runs inside the capture: any CUDA work it issues is captured into
the graph, and under the default `"global"` capture error mode an unsafe
call raises. See [`torch.cuda.graphs.register_graph_capture_start_hook()`](torch.cuda.graphs.register_graph_capture_start_hook.html#torch.cuda.graphs.register_graph_capture_start_hook).

Return type:

RemovableHandle

register_destroy_callback(*cb*, ***, *synchronize_before_release=False*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L485)

Register `cb()` to run when this graph is destroyed (finalized) or
explicitly `reset()`, just before its CUDA resources are freed.
Callbacks fire once per capture cycle, in registration order; exceptions
are swallowed so one failure does not abort the rest. `cb` must NOT
reference this graph: the finalizer that fires it is held by a global
registry, so a callback reachable to the graph keeps the graph alive
until interpreter exit (it is never collected, hence never fired).
Returns a handle whose `remove()` deregisters the callback.

Teardown does not synchronize CUDA, and `cudaGraphExecDestroy` frees an
in-flight graph only asynchronously, so a callback that frees device
memory the graph reads/writes is a use-after-free if a replay is still
in flight. Pass `synchronize_before_release=True` to synchronize every
stream this graph was replayed on before firing. Otherwise callbacks
must not free anything the graph references.

Return type:

RemovableHandle

register_post_instantiate_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L431)

Register `hook(graph)` to run after each instantiation (including
re-instantiation, which produces a fresh exec graph). The instantiated
graph is available via `raw_cuda_graph_exec()`. Hooks fire in
registration order. Returns a handle whose `remove()` deregisters the
hook.

Return type:

RemovableHandle

register_replay_end_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L465)

Register `hook(graph)` to run at the end of every `replay()`,
just after the graph is launched. The launch is asynchronous, so the hook
runs once the replay is *enqueued*, not once the GPU work completes. Hooks
fire in registration order. Returns a handle whose `remove()`
deregisters the hook. See the hot-path note on
`register_replay_start_hook()`.

End hooks fire even if the launch raises - so a start hook is always
balanced by an end - and the launch error then propagates. (Start hooks
that raise abort the replay before launch, and no end hook fires.)

Return type:

RemovableHandle

register_replay_start_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L446)

Register `hook(graph)` to run at the start of every `replay()`,
just before the graph is launched (after any on-demand instantiation, so
`raw_cuda_graph_exec()` is valid). Hooks fire in registration order.
Returns a handle whose `remove()` deregisters the hook.

Note

Replay is the hot path and a registered hook runs on every replay -
keep it cheap. With no hook registered the cost is a single dict
emptiness check.

Return type:

RemovableHandle

replay()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L688)

Replay the CUDA work captured by this graph.

reset()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L716)

Delete the graph currently held by this instance.

retain_object(*obj*, ***, *synchronize_before_release=False*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/cuda/graphs.py#L515)

Keep `obj` alive for this graph's current capture cycle and release
it when the graph is destroyed (finalized) or explicitly `reset()`.
No callback runs; normal refcounting drops `obj` when the retained
reference is released. Returns a handle whose `remove()` drops the
retained reference early. As with `register_destroy_callback()`,
`obj` must NOT reference this graph, or the graph is kept alive until
interpreter exit and `obj` is never released.

`synchronize_before_release` has the same meaning and caveats as in
`register_destroy_callback()`: set it if releasing `obj` frees device
memory the graph reads/writes (e.g. `obj` is the last reference to a
tensor the graph uses) and replays may still be in flight.

Return type:

RemovableHandle