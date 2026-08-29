# torch.xpu

This package introduces support for the XPU backend, specifically tailored for
Intel GPU optimization.

This package is lazily initialized, so you can always import it, and use
[`is_available()`](generated/torch.xpu.is_available.html#torch.xpu.is_available) to determine if your system supports XPU.

| [`StreamContext`](generated/torch.xpu.StreamContext.html#torch.xpu.StreamContext) | Context-manager that selects a given stream. |
| --- | --- |
| [`can_device_access_peer`](generated/torch.xpu.can_device_access_peer.html#torch.xpu.can_device_access_peer) | Query whether a device can access a peer device's memory. |
| [`clock_rate`](generated/torch.xpu.clock_rate.html#torch.xpu.clock_rate) | Return the GPU clock rate in MHz. |
| [`current_device`](generated/torch.xpu.current_device.html#torch.xpu.current_device) | Return the index of a currently selected device. |
| [`current_stream`](generated/torch.xpu.current_stream.html#torch.xpu.current_stream) | Return the currently selected [`Stream`](generated/torch.xpu.Stream_class.html#torch.xpu.Stream) for a given device. |
| [`device`](generated/torch.xpu.device.html#torch.xpu.device) | Context-manager that changes the selected device. |
| [`device_count`](generated/torch.xpu.device_count.html#torch.xpu.device_count) | Return the number of XPU device available. |
| [`device_of`](generated/torch.xpu.device_of.html#torch.xpu.device_of) | Context-manager that changes the current device to that of given object. |
| [`device_memory_used`](generated/torch.xpu.device_memory_used.html#torch.xpu.device_memory_used) | Return the current GPU used global (device) memory in bytes. |
| [`get_arch_list`](generated/torch.xpu.get_arch_list.html#torch.xpu.get_arch_list) | Return list XPU architectures this library was compiled for. |
| [`get_device_capability`](generated/torch.xpu.get_device_capability.html#torch.xpu.get_device_capability) | Get the xpu capability of a device. |
| [`get_device_name`](generated/torch.xpu.get_device_name.html#torch.xpu.get_device_name) | Get the name of a device. |
| [`get_device_properties`](generated/torch.xpu.get_device_properties.html#torch.xpu.get_device_properties) | Get the properties of a device. |
| [`get_gencode_flags`](generated/torch.xpu.get_gencode_flags.html#torch.xpu.get_gencode_flags) | Return XPU AOT(ahead-of-time) build flags this library was compiled with. |
| [`get_stream_from_external`](generated/torch.xpu.get_stream_from_external.html#torch.xpu.get_stream_from_external) | Return a [`Stream`](generated/torch.xpu.Stream_class.html#torch.xpu.Stream) from an external SYCL queue. |
| [`init`](generated/torch.xpu.init.html#torch.xpu.init) | Initialize PyTorch's XPU state. |
| [`is_available`](generated/torch.xpu.is_available.html#torch.xpu.is_available) | Return a bool indicating if XPU is currently available. |
| [`is_bf16_supported`](generated/torch.xpu.is_bf16_supported.html#torch.xpu.is_bf16_supported) | Return a bool indicating if the current XPU device supports dtype bfloat16. |
| [`is_initialized`](generated/torch.xpu.is_initialized.html#torch.xpu.is_initialized) | Return whether PyTorch's XPU state has been initialized. |
| [`is_tf32_supported`](generated/torch.xpu.is_tf32_supported.html#torch.xpu.is_tf32_supported) | Return a bool indicating if the current XPU device supports dtype tf32. |
| [`memory_usage`](generated/torch.xpu.memory_usage.html#torch.xpu.memory_usage) | Return the GPU memory bandwidth usage as a percentage. |
| [`power_draw`](generated/torch.xpu.power_draw.html#torch.xpu.power_draw) | Return the GPU card power draw in watts. |
| [`set_device`](generated/torch.xpu.set_device.html#torch.xpu.set_device) | Set the current device. |
| [`set_stream`](generated/torch.xpu.set_stream.html#torch.xpu.set_stream) | Set the current stream. This is a wrapper API to set the stream. |
| [`stream`](generated/torch.xpu.stream_function.html#torch.xpu.stream) | Wrap around the Context-manager StreamContext that selects a given stream. |
| [`synchronize`](generated/torch.xpu.synchronize.html#torch.xpu.synchronize) | Wait for all kernels in all streams on a XPU device to complete. |
| [`temperature`](generated/torch.xpu.temperature.html#torch.xpu.temperature) | Return the GPU temperature in degrees Celsius. |
| [`utilization`](generated/torch.xpu.utilization.html#torch.xpu.utilization) | Return the GPU engine utilization as a percentage. |

## Random Number Generator

| [`get_rng_state`](generated/torch.xpu.get_rng_state.html#torch.xpu.get_rng_state) | Return the random number generator state of the specified GPU as a ByteTensor. |
| --- | --- |
| [`get_rng_state_all`](generated/torch.xpu.get_rng_state_all.html#torch.xpu.get_rng_state_all) | Return a list of ByteTensor representing the random number states of all devices. |
| [`initial_seed`](generated/torch.xpu.initial_seed.html#torch.xpu.initial_seed) | Return the current random seed of the current GPU. |
| [`manual_seed`](generated/torch.xpu.manual_seed.html#torch.xpu.manual_seed) | Set the seed for generating random numbers for the current GPU. |
| [`manual_seed_all`](generated/torch.xpu.manual_seed_all.html#torch.xpu.manual_seed_all) | Set the seed for generating random numbers on all GPUs. |
| [`seed`](generated/torch.xpu.seed.html#torch.xpu.seed) | Set the seed for generating random numbers to a random number for the current GPU. |
| [`seed_all`](generated/torch.xpu.seed_all.html#torch.xpu.seed_all) | Set the seed for generating random numbers to a random number on all GPUs. |
| [`set_rng_state`](generated/torch.xpu.set_rng_state.html#torch.xpu.set_rng_state) | Set the random number generator state of the specified GPU. |
| [`set_rng_state_all`](generated/torch.xpu.set_rng_state_all.html#torch.xpu.set_rng_state_all) | Set the random number generator state of all devices. |

## Streams and events

| [`Event`](generated/torch.xpu.Event.html#torch.xpu.Event) | Wrapper around a XPU event. |
| --- | --- |
| [`Stream`](generated/torch.xpu.Stream_class.html#torch.xpu.Stream) | Wrapper around a XPU stream. |

## Graphs

| [`is_current_stream_capturing`](generated/torch.xpu.is_current_stream_capturing.html#torch.xpu.is_current_stream_capturing) | Return True if XPU graph capture is underway on the current XPU stream, False otherwise. |
| --- | --- |
| [`graph_pool_handle`](generated/torch.xpu.graph_pool_handle.html#torch.xpu.graph_pool_handle) | Return an opaque token representing the id of a graph memory pool. |
| [`XPUGraph`](generated/torch.xpu.XPUGraph.html#torch.xpu.XPUGraph) | Wrapper around a XPU graph. |
| [`graph`](generated/torch.xpu.graph.html#torch.xpu.graph) | Context-manager that captures XPU work into a [`torch.xpu.XPUGraph`](generated/torch.xpu.XPUGraph.html#torch.xpu.XPUGraph) object for later replay. |
| [`make_graphed_callables`](generated/torch.xpu.make_graphed_callables.html#torch.xpu.make_graphed_callables) | Accept callables (functions or [`nn.Module`](generated/torch.nn.Module.html#torch.nn.Module)s) and returns graphed versions. |

## Memory management

| [`XPUPluggableAllocator`](generated/torch.xpu.memory.XPUPluggableAllocator.html#torch.xpu.memory.XPUPluggableAllocator) | XPU memory allocator loaded dynamically from a shared library. |
| --- | --- |
| [`change_current_allocator`](generated/torch.xpu.memory.change_current_allocator.html#torch.xpu.memory.change_current_allocator) | Change the currently used memory allocator to be the one provided. |
| [`empty_cache`](generated/torch.xpu.memory.empty_cache.html#torch.xpu.memory.empty_cache) | Release all unoccupied cached memory currently held by the caching allocator so that those can be used in other XPU application. |
| [`get_per_process_memory_fraction`](generated/torch.xpu.memory.get_per_process_memory_fraction.html#torch.xpu.memory.get_per_process_memory_fraction) | Retrieve the memory fraction currently set for a process on a given XPU device. |
| [`list_gpu_processes`](generated/torch.xpu.memory.list_gpu_processes.html#torch.xpu.memory.list_gpu_processes) | Return a printout of running processes and their GPU memory usage on a given device. |
| [`max_memory_allocated`](generated/torch.xpu.memory.max_memory_allocated.html#torch.xpu.memory.max_memory_allocated) | Return the maximum GPU memory occupied by tensors in bytes for a given device. |
| [`max_memory_reserved`](generated/torch.xpu.memory.max_memory_reserved.html#torch.xpu.memory.max_memory_reserved) | Return the maximum GPU memory managed by the caching allocator in bytes for a given device. |
| [`mem_get_info`](generated/torch.xpu.memory.mem_get_info.html#torch.xpu.memory.mem_get_info) | Return the global free and total GPU memory for a given device. |
| [`memory_allocated`](generated/torch.xpu.memory.memory_allocated.html#torch.xpu.memory.memory_allocated) | Return the current GPU memory occupied by tensors in bytes for a given device. |
| [`memory_reserved`](generated/torch.xpu.memory.memory_reserved.html#torch.xpu.memory.memory_reserved) | Return the current GPU memory managed by the caching allocator in bytes for a given device. |
| [`memory_snapshot`](generated/torch.xpu.memory.memory_snapshot.html#torch.xpu.memory.memory_snapshot) | Return a snapshot of the XPU memory allocator state across all devices. |
| [`memory_stats`](generated/torch.xpu.memory.memory_stats.html#torch.xpu.memory.memory_stats) | Return a dictionary of XPU memory allocator statistics for a given device. |
| [`memory_stats_as_nested_dict`](generated/torch.xpu.memory.memory_stats_as_nested_dict.html#torch.xpu.memory.memory_stats_as_nested_dict) | Return the result of `memory_stats()` as a nested dictionary. |
| [`reset_accumulated_memory_stats`](generated/torch.xpu.memory.reset_accumulated_memory_stats.html#torch.xpu.memory.reset_accumulated_memory_stats) | Reset the "accumulated" (historical) stats tracked by the XPU memory allocator. |
| [`reset_peak_memory_stats`](generated/torch.xpu.memory.reset_peak_memory_stats.html#torch.xpu.memory.reset_peak_memory_stats) | Reset the "peak" stats tracked by the XPU memory allocator. |
| [`set_per_process_memory_fraction`](generated/torch.xpu.memory.set_per_process_memory_fraction.html#torch.xpu.memory.set_per_process_memory_fraction) | Set the memory fraction for a single process on XPU device. |
| [`MemPool`](generated/torch.xpu.memory.MemPool.html#torch.xpu.memory.MemPool) | MemPool represents a pool of memory in a caching allocator. |

*class*torch.xpu.use_mem_pool(*pool*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/fe3f518c806b6f1fb8acc283135e5414b8606887/torch/xpu/memory.py#L600)

A context manager that routes allocations to a given pool.

Parameters:

- **pool** (*torch.xpu.MemPool*) - a `MemPool` object to be made active so that
allocations route to this pool.
- **device** ([*torch.device*](tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Uses `MemPool` on
the current device, given by [`current_device()`](generated/torch.xpu.current_device.html#torch.xpu.current_device),
if [`device`](generated/torch.xpu.device.html#torch.xpu.device) is `None` (default).

Note

This context manager makes only current thread's allocations route to
the given pool. If a new thread is spawned inside the context manager
(e.g. by calling backward) the allocations in that thread will not
route to the given pool.