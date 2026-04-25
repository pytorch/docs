# Aliases in torch.cuda

The following are aliases to their counterparts in `torch.cuda` in the nested namespaces in which they are defined. For any of these APIs, feel free to use the top-level version in `torch.cuda` like `torch.cuda.seed` or the nested version `torch.cuda.random.seed`.

| [`get_rng_state`](generated/torch.cuda.random.get_rng_state.html#torch.cuda.random.get_rng_state) | Return the random number generator state of the specified GPU as a ByteTensor. |
| --- | --- |
| [`get_rng_state_all`](generated/torch.cuda.random.get_rng_state_all.html#torch.cuda.random.get_rng_state_all) | Return a list of ByteTensor representing the random number states of all devices. |
| [`set_rng_state`](generated/torch.cuda.random.set_rng_state.html#torch.cuda.random.set_rng_state) | Set the random number generator state of the specified GPU. |
| [`set_rng_state_all`](generated/torch.cuda.random.set_rng_state_all.html#torch.cuda.random.set_rng_state_all) | Set the random number generator state of all devices. |
| [`manual_seed`](generated/torch.cuda.random.manual_seed.html#torch.cuda.random.manual_seed) | Set the seed for generating random numbers for the current GPU. |
| [`manual_seed_all`](generated/torch.cuda.random.manual_seed_all.html#torch.cuda.random.manual_seed_all) | Set the seed for generating random numbers on all GPUs. |
| [`seed`](generated/torch.cuda.random.seed.html#torch.cuda.random.seed) | Set the seed for generating random numbers to a random number for the current GPU. |
| [`seed_all`](generated/torch.cuda.random.seed_all.html#torch.cuda.random.seed_all) | Set the seed for generating random numbers to a random number on all GPUs. |
| [`initial_seed`](generated/torch.cuda.random.initial_seed.html#torch.cuda.random.initial_seed) | Return the current random seed of the current GPU. |

| [`is_current_stream_capturing`](generated/torch.cuda.graphs.is_current_stream_capturing.html#torch.cuda.graphs.is_current_stream_capturing) | Return True if CUDA graph capture is underway on the current CUDA stream, False otherwise. |
| --- | --- |
| [`graph_pool_handle`](generated/torch.cuda.graphs.graph_pool_handle.html#torch.cuda.graphs.graph_pool_handle) | Return an opaque token representing the id of a graph memory pool. |
| [`CUDAGraph`](generated/torch.cuda.graphs.CUDAGraph.html#torch.cuda.graphs.CUDAGraph) | Wrapper around a CUDA graph. |
| [`graph`](generated/torch.cuda.graphs.graph.html#torch.cuda.graphs.graph) | Context-manager that captures CUDA work into a [`torch.cuda.CUDAGraph`](generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph) object for later replay. |
| [`make_graphed_callables`](generated/torch.cuda.graphs.make_graphed_callables.html#torch.cuda.graphs.make_graphed_callables) | Accept callables (functions or [`nn.Module`](generated/torch.nn.Module.html#torch.nn.Module)s) and returns graphed versions. |

| [`Stream`](generated/torch.cuda.streams.Stream.html#torch.cuda.streams.Stream) | Wrapper around a CUDA stream. |
| --- | --- |
| [`ExternalStream`](generated/torch.cuda.streams.ExternalStream.html#torch.cuda.streams.ExternalStream) | Wrapper around an externally allocated CUDA stream. |
| [`Event`](generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event) | Wrapper around a CUDA event. |