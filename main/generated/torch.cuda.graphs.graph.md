# graph

*class*torch.cuda.graphs.graph(*cuda_graph*, *pool=None*, *stream=None*, *capture_error_mode='global'*, *enable_annotations=False*, *annotation_config=None*, *check_input_liveness=False*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/cuda/graphs.py#L1117)

Context-manager that captures CUDA work into a [`torch.cuda.CUDAGraph`](torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph) object for later replay.

See [CUDA Graphs](../notes/cuda.html#cuda-graph-semantics) for a general introduction,
detailed use, and constraints.

Parameters:

- **cuda_graph** ([*torch.cuda.CUDAGraph*](torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph)) - Graph object used for capture.
- **pool** (*optional*) - Opaque token (returned by a call to [`graph_pool_handle()`](torch.cuda.graph_pool_handle.html#torch.cuda.graph_pool_handle) or
[`other_Graph_instance.pool()`](torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.pool)) or
`MemPool` hinting this graph's capture may share memory
from the specified pool. See [Graph memory management](../notes/cuda.html#graph-memory-management).
- **stream** ([*torch.cuda.Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)*,**optional*) - If supplied, will be set as the current stream in the context.
If not supplied, `graph` sets its own internal side stream as the current stream in the context.
- **capture_error_mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - specifies the cudaStreamCaptureMode for the graph capture stream.
Can be "global", "thread_local" or "relaxed". During cuda graph capture, some actions, such as cudaMalloc,
may be unsafe. "global" will error on actions in other threads, "thread_local" will only error for
actions in the current thread, and "relaxed" will not error on actions. Do NOT change this setting
unless you're familiar with [cudaStreamCaptureMode](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html#group__CUDART__STREAM_1g9d0535d93a214cbf126835257b16ba85)
- **enable_annotations** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True`, enables kernel annotation
recording on entry and automatically calls
`resolve_pending_annotations()` before
the capture ends. Annotations are **not** cleared on exit so that multiple
graphs in the same workload can accumulate annotations.
Requires `cuda.bindings` package and cuda-compat >= 13.1 or CUDA driver >= 13.1.
Requires single-threaded autograd; wrap the capture in
`torch.autograd.grad_mode.set_multithreading_enabled(False)`.
- **annotation_config** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*,**optional*) - Options for annotation recording, used when
`enable_annotations=True`. An unrecognized key or value raises. Currently
supports `"backend"`, which selects how `mark_kernels` scopes discover their
nodes: `"auto"` (default) uses CUPTI node-creation callbacks when the CUPTI
monitor already holds a subscription and otherwise walks the capture graph's
dependent edges; `"cupti"` requires the CUPTI path, bringing the monitor up if
needed - which prevents kineto from initializing, so a later
[`torch.profiler.profile`](../profiler.html#torch.profiler.profile) records no GPU activity; `"edge_walk"` forces
the walk, which cannot see nodes created while the current stream was not yet
capturing.
- **check_input_liveness** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) -

If `True`, tracks external tensor inputs during graph capture and
raises an error if any are deallocated before replay. This helps debug "use after free" errors
where input tensors are garbage collected between capture and replay. Default: `False`.

Note

Custom CUDA kernels added outside PyTorch (e.g., via cuLaunchKernel or DLPack) are not
tracked by this mechanism.

Note

For effective memory sharing, if you pass a `pool` used by a previous capture and the previous capture
used an explicit `stream` argument, you should pass the same `stream` argument to this capture.

Warning

This API is in beta and may change in future releases.