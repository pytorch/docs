# Aliases in torch.xpu

The following are aliases to their counterparts in `torch.xpu` in the nested namespaces in which they are defined. For any of these APIs, feel free to use the top-level version in `torch.xpu` like `torch.xpu.seed` or the nested version `torch.xpu.random.seed`.

| [`get_rng_state`](generated/torch.xpu.random.get_rng_state.html#torch.xpu.random.get_rng_state) | Return the random number generator state of the specified GPU as a ByteTensor. |
| --- | --- |
| [`get_rng_state_all`](generated/torch.xpu.random.get_rng_state_all.html#torch.xpu.random.get_rng_state_all) | Return a list of ByteTensor representing the random number states of all devices. |
| [`initial_seed`](generated/torch.xpu.random.initial_seed.html#torch.xpu.random.initial_seed) | Return the current random seed of the current GPU. |
| [`manual_seed`](generated/torch.xpu.random.manual_seed.html#torch.xpu.random.manual_seed) | Set the seed for generating random numbers for the current GPU. |
| [`manual_seed_all`](generated/torch.xpu.random.manual_seed_all.html#torch.xpu.random.manual_seed_all) | Set the seed for generating random numbers on all GPUs. |
| [`seed`](generated/torch.xpu.random.seed.html#torch.xpu.random.seed) | Set the seed for generating random numbers to a random number for the current GPU. |
| [`seed_all`](generated/torch.xpu.random.seed_all.html#torch.xpu.random.seed_all) | Set the seed for generating random numbers to a random number on all GPUs. |
| [`set_rng_state`](generated/torch.xpu.random.set_rng_state.html#torch.xpu.random.set_rng_state) | Set the random number generator state of the specified GPU. |
| [`set_rng_state_all`](generated/torch.xpu.random.set_rng_state_all.html#torch.xpu.random.set_rng_state_all) | Set the random number generator state of all devices. |

| [`is_current_stream_capturing`](generated/torch.xpu.graphs.is_current_stream_capturing.html#torch.xpu.graphs.is_current_stream_capturing) | Return True if XPU graph capture is underway on the current XPU stream, False otherwise. |
| --- | --- |
| [`graph_pool_handle`](generated/torch.xpu.graphs.graph_pool_handle.html#torch.xpu.graphs.graph_pool_handle) | Return an opaque token representing the id of a graph memory pool. |
| [`XPUGraph`](generated/torch.xpu.graphs.XPUGraph.html#torch.xpu.graphs.XPUGraph) | Wrapper around a XPU graph. |
| [`graph`](generated/torch.xpu.graphs.graph.html#torch.xpu.graphs.graph) | Context-manager that captures XPU work into a [`torch.xpu.XPUGraph`](generated/torch.xpu.XPUGraph.html#torch.xpu.XPUGraph) object for later replay. |
| [`make_graphed_callables`](generated/torch.xpu.graphs.make_graphed_callables.html#torch.xpu.graphs.make_graphed_callables) | Accept callables (functions or [`nn.Module`](generated/torch.nn.Module.html#torch.nn.Module)s) and returns graphed versions. |

| [`Event`](generated/torch.xpu.streams.Event.html#torch.xpu.streams.Event) | Wrapper around a XPU event. |
| --- | --- |
| [`Stream`](generated/torch.xpu.streams.Stream.html#torch.xpu.streams.Stream) | Wrapper around a XPU stream. |