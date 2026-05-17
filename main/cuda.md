# torch.cuda

This package adds support for CUDA tensor types.

It implements the same function as CPU tensors, but they utilize
GPUs for computation.

It is lazily initialized, so you can always import it, and use
[`is_available()`](generated/torch.cuda.is_available.html#torch.cuda.is_available) to determine if your system supports CUDA.

[CUDA semantics](notes/cuda.html#cuda-semantics) has more details about working with CUDA.

| [`StreamContext`](generated/torch.cuda.StreamContext.html#torch.cuda.StreamContext) | Context-manager that selects a given stream. |
| --- | --- |
| [`can_device_access_peer`](generated/torch.cuda.can_device_access_peer.html#torch.cuda.can_device_access_peer) | Check if peer access between two devices is possible. |
| [`check_error`](generated/torch.cuda.check_error.html#torch.cuda.check_error) | Raise an error if the result of a CUDA runtime API call is not success. |
| [`current_blas_handle`](generated/torch.cuda.current_blas_handle.html#torch.cuda.current_blas_handle) | Return cublasHandle_t pointer to current cuBLAS handle |
| [`current_device`](generated/torch.cuda.current_device.html#torch.cuda.current_device) | Return the index of a currently selected device. |
| [`current_stream`](generated/torch.cuda.current_stream.html#torch.cuda.current_stream) | Return the currently selected [`Stream`](generated/torch.cuda.Stream_class.html#torch.cuda.Stream) for a given device. |
| [`cudart`](generated/torch.cuda.cudart.html#torch.cuda.cudart) | Retrieves the CUDA runtime API module. |
| [`default_stream`](generated/torch.cuda.default_stream.html#torch.cuda.default_stream) | Return the default [`Stream`](generated/torch.cuda.Stream_class.html#torch.cuda.Stream) for a given device. |
| [`device`](generated/torch.cuda.device.html#torch.cuda.device) | Context-manager that changes the selected device. |
| [`device_count`](generated/torch.cuda.device_count.html#torch.cuda.device_count) | Return the number of GPUs available. |
| [`device_memory_used`](generated/torch.cuda.device_memory_used.html#torch.cuda.device_memory_used) | Return used global (device) memory in bytes as given by nvidia-smi or amd-smi. |
| [`device_of`](generated/torch.cuda.device_of.html#torch.cuda.device_of) | Context-manager that changes the current device to that of given object. |
| [`get_arch_list`](generated/torch.cuda.get_arch_list.html#torch.cuda.get_arch_list) | Return list CUDA architectures this library was compiled for. |
| [`get_device_capability`](generated/torch.cuda.get_device_capability.html#torch.cuda.get_device_capability) | Get the cuda capability of a device. |
| [`get_device_name`](generated/torch.cuda.get_device_name.html#torch.cuda.get_device_name) | Get the name of a device. |
| [`get_device_properties`](generated/torch.cuda.get_device_properties.html#torch.cuda.get_device_properties) | Get the properties of a device. |
| [`get_gencode_flags`](generated/torch.cuda.get_gencode_flags.html#torch.cuda.get_gencode_flags) | Return NVCC gencode flags this library was compiled with. |
| [`get_stream_from_external`](generated/torch.cuda.get_stream_from_external.html#torch.cuda.get_stream_from_external) | Return a [`Stream`](generated/torch.cuda.Stream_class.html#torch.cuda.Stream) from an externally allocated CUDA stream. |
| [`get_sync_debug_mode`](generated/torch.cuda.get_sync_debug_mode.html#torch.cuda.get_sync_debug_mode) | Return current value of debug mode for cuda synchronizing operations. |
| [`init`](generated/torch.cuda.init.html#torch.cuda.init) | Initialize PyTorch's CUDA state. |
| [`ipc_collect`](generated/torch.cuda.ipc_collect.html#torch.cuda.ipc_collect) | Force collects GPU memory after it has been released by CUDA IPC. |
| [`is_available`](generated/torch.cuda.is_available.html#torch.cuda.is_available) | Return a bool indicating if CUDA is currently available. |
| [`is_bf16_supported`](generated/torch.cuda.is_bf16_supported.html#torch.cuda.is_bf16_supported) | Return a bool indicating if the current CUDA/ROCm device supports dtype bfloat16. |
| [`is_initialized`](generated/torch.cuda.is_initialized.html#torch.cuda.is_initialized) | Return whether PyTorch's CUDA state has been initialized. |
| [`is_tf32_supported`](generated/torch.cuda.is_tf32_supported.html#torch.cuda.is_tf32_supported) | Return a bool indicating if the current CUDA/ROCm device supports dtype tf32. |
| [`memory_usage`](generated/torch.cuda.memory_usage.html#torch.cuda.memory_usage) | Return the percent of time over the past sample period during which global (device) memory was being read or written as given by nvidia-smi. |
| [`set_device`](generated/torch.cuda.set_device.html#torch.cuda.set_device) | Set the current device. |
| [`set_stream`](generated/torch.cuda.set_stream.html#torch.cuda.set_stream) | Set the current stream. This is a wrapper API to set the stream. |
| [`set_sync_debug_mode`](generated/torch.cuda.set_sync_debug_mode.html#torch.cuda.set_sync_debug_mode) | Set the debug mode for cuda synchronizing operations. |
| [`stream`](generated/torch.cuda.stream_function.html#torch.cuda.stream) | Wrap around the Context-manager StreamContext that selects a given stream. |
| [`synchronize`](generated/torch.cuda.synchronize.html#torch.cuda.synchronize) | Wait for all kernels in all streams on a CUDA device to complete. |
| [`utilization`](generated/torch.cuda.utilization.html#torch.cuda.utilization) | Return the percent of time over the past sample period during which one or more kernels was executing on the GPU as given by nvidia-smi. |
| [`temperature`](generated/torch.cuda.temperature.html#torch.cuda.temperature) | Return the average temperature of the GPU sensor in Degrees C (Centigrades). |
| [`power_draw`](generated/torch.cuda.power_draw.html#torch.cuda.power_draw) | Return the average power draw of the GPU sensor in mW (MilliWatts) |
| [`clock_rate`](generated/torch.cuda.clock_rate.html#torch.cuda.clock_rate) | Return the clock speed of the GPU SM in MHz (megahertz) over the past sample period as given by nvidia-smi. |
| [`AcceleratorError`](generated/torch.cuda.AcceleratorError.html#torch.cuda.AcceleratorError) | Exception raised while executing on device |
| [`OutOfMemoryError`](generated/torch.cuda.OutOfMemoryError.html#torch.cuda.OutOfMemoryError) | Exception raised when device is out of memory |

## Random Number Generator

| [`get_rng_state`](generated/torch.cuda.get_rng_state.html#torch.cuda.get_rng_state) | Return the random number generator state of the specified GPU as a ByteTensor. |
| --- | --- |
| [`get_rng_state_all`](generated/torch.cuda.get_rng_state_all.html#torch.cuda.get_rng_state_all) | Return a list of ByteTensor representing the random number states of all devices. |
| [`set_rng_state`](generated/torch.cuda.set_rng_state.html#torch.cuda.set_rng_state) | Set the random number generator state of the specified GPU. |
| [`set_rng_state_all`](generated/torch.cuda.set_rng_state_all.html#torch.cuda.set_rng_state_all) | Set the random number generator state of all devices. |
| [`manual_seed`](generated/torch.cuda.manual_seed.html#torch.cuda.manual_seed) | Set the seed for generating random numbers for the current GPU. |
| [`manual_seed_all`](generated/torch.cuda.manual_seed_all.html#torch.cuda.manual_seed_all) | Set the seed for generating random numbers on all GPUs. |
| [`seed`](generated/torch.cuda.seed.html#torch.cuda.seed) | Set the seed for generating random numbers to a random number for the current GPU. |
| [`seed_all`](generated/torch.cuda.seed_all.html#torch.cuda.seed_all) | Set the seed for generating random numbers to a random number on all GPUs. |
| [`initial_seed`](generated/torch.cuda.initial_seed.html#torch.cuda.initial_seed) | Return the current random seed of the current GPU. |

## Communication collectives

| [`comm.broadcast`](generated/torch.cuda.comm.broadcast.html#torch.cuda.comm.broadcast) | Broadcasts a tensor to specified GPU devices. |
| --- | --- |
| [`comm.broadcast_coalesced`](generated/torch.cuda.comm.broadcast_coalesced.html#torch.cuda.comm.broadcast_coalesced) | Broadcast a sequence of tensors to the specified GPUs. |
| [`comm.reduce_add`](generated/torch.cuda.comm.reduce_add.html#torch.cuda.comm.reduce_add) | Sum tensors from multiple GPUs. |
| [`comm.reduce_add_coalesced`](generated/torch.cuda.comm.reduce_add_coalesced.html#torch.cuda.comm.reduce_add_coalesced) | Sum tensors from multiple GPUs. |
| [`comm.scatter`](generated/torch.cuda.comm.scatter.html#torch.cuda.comm.scatter) | Scatters tensor across multiple GPUs. |
| [`comm.gather`](generated/torch.cuda.comm.gather.html#torch.cuda.comm.gather) | Gathers tensors from multiple GPU devices. |

## Streams and events

| [`Stream`](generated/torch.cuda.Stream_class.html#torch.cuda.Stream) | Wrapper around a CUDA stream. |
| --- | --- |
| [`ExternalStream`](generated/torch.cuda.ExternalStream.html#torch.cuda.ExternalStream) | Wrapper around an externally allocated CUDA stream. |
| [`Event`](generated/torch.cuda.Event.html#torch.cuda.Event) | Wrapper around a CUDA event. |

## Graphs (beta)

| [`is_current_stream_capturing`](generated/torch.cuda.is_current_stream_capturing.html#torch.cuda.is_current_stream_capturing) | Return True if CUDA graph capture is underway on the current CUDA stream, False otherwise. |
| --- | --- |
| [`graph_pool_handle`](generated/torch.cuda.graph_pool_handle.html#torch.cuda.graph_pool_handle) | Return an opaque token representing the id of a graph memory pool. |
| [`CUDAGraph`](generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph) | Wrapper around a CUDA graph. |
| [`graph`](generated/torch.cuda.graph.html#torch.cuda.graph) | Context-manager that captures CUDA work into a [`torch.cuda.CUDAGraph`](generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph) object for later replay. |
| [`make_graphed_callables`](generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables) | Accept callables (functions or [`nn.Module`](generated/torch.nn.Module.html#torch.nn.Module)s) and returns graphed versions. |

This package adds support for device memory management implemented in CUDA.

## Memory management

| [`empty_cache`](generated/torch.cuda.memory.empty_cache.html#torch.cuda.memory.empty_cache) | Release all unoccupied cached memory currently held by the caching allocator so that those can be used in other GPU application and visible in nvidia-smi. |
| --- | --- |
| [`get_per_process_memory_fraction`](generated/torch.cuda.memory.get_per_process_memory_fraction.html#torch.cuda.memory.get_per_process_memory_fraction) | Get memory fraction for a process. |
| [`list_gpu_processes`](generated/torch.cuda.memory.list_gpu_processes.html#torch.cuda.memory.list_gpu_processes) | Return a human-readable printout of the running processes and their GPU memory use for a given device. |
| [`mem_get_info`](generated/torch.cuda.memory.mem_get_info.html#torch.cuda.memory.mem_get_info) | Return the global free and total GPU memory for a given device using cudaMemGetInfo. |
| [`memory_stats`](generated/torch.cuda.memory.memory_stats.html#torch.cuda.memory.memory_stats) | Return a dictionary of CUDA memory allocator statistics for a given device. |
| [`memory_stats_as_nested_dict`](generated/torch.cuda.memory.memory_stats_as_nested_dict.html#torch.cuda.memory.memory_stats_as_nested_dict) | Return the result of `memory_stats()` as a nested dictionary. |
| [`reset_accumulated_memory_stats`](generated/torch.cuda.memory.reset_accumulated_memory_stats.html#torch.cuda.memory.reset_accumulated_memory_stats) | Reset the "accumulated" (historical) stats tracked by the CUDA memory allocator. |
| [`host_memory_stats`](generated/torch.cuda.memory.host_memory_stats.html#torch.cuda.memory.host_memory_stats) | Return a dictionary of pinned (host) allocator statistics. |
| [`host_memory_stats_as_nested_dict`](generated/torch.cuda.memory.host_memory_stats_as_nested_dict.html#torch.cuda.memory.host_memory_stats_as_nested_dict) | Return the result of `host_memory_stats()` as a nested dictionary. |
| [`reset_accumulated_host_memory_stats`](generated/torch.cuda.memory.reset_accumulated_host_memory_stats.html#torch.cuda.memory.reset_accumulated_host_memory_stats) | Reset the "accumulated" (historical) stats tracked by the host memory allocator. |
| [`memory_summary`](generated/torch.cuda.memory.memory_summary.html#torch.cuda.memory.memory_summary) | Return a human-readable printout of the current memory allocator statistics for a given device. |
| [`memory_snapshot`](generated/torch.cuda.memory.memory_snapshot.html#torch.cuda.memory.memory_snapshot) | Return a snapshot of the CUDA memory allocator state across all devices. |
| [`memory_allocated`](generated/torch.cuda.memory.memory_allocated.html#torch.cuda.memory.memory_allocated) | Return the current GPU memory occupied by tensors in bytes for a given device. |
| [`max_memory_allocated`](generated/torch.cuda.memory.max_memory_allocated.html#torch.cuda.memory.max_memory_allocated) | Return the maximum GPU memory occupied by tensors in bytes for a given device. |
| [`reset_max_memory_allocated`](generated/torch.cuda.memory.reset_max_memory_allocated.html#torch.cuda.memory.reset_max_memory_allocated) | Reset the starting point in tracking maximum GPU memory occupied by tensors for a given device. |
| [`memory_reserved`](generated/torch.cuda.memory.memory_reserved.html#torch.cuda.memory.memory_reserved) | Return the current GPU memory managed by the caching allocator in bytes for a given device. |
| [`max_memory_reserved`](generated/torch.cuda.memory.max_memory_reserved.html#torch.cuda.memory.max_memory_reserved) | Return the maximum GPU memory managed by the caching allocator in bytes for a given device. |
| [`set_per_process_memory_fraction`](generated/torch.cuda.memory.set_per_process_memory_fraction.html#torch.cuda.memory.set_per_process_memory_fraction) | Set memory fraction for a process. |
| [`memory_cached`](generated/torch.cuda.memory.memory_cached.html#torch.cuda.memory.memory_cached) | Deprecated; see `memory_reserved()`. |
| [`max_memory_cached`](generated/torch.cuda.memory.max_memory_cached.html#torch.cuda.memory.max_memory_cached) | Deprecated; see `max_memory_reserved()`. |
| [`reset_max_memory_cached`](generated/torch.cuda.memory.reset_max_memory_cached.html#torch.cuda.memory.reset_max_memory_cached) | Reset the starting point in tracking maximum GPU memory managed by the caching allocator for a given device. |
| [`reset_peak_memory_stats`](generated/torch.cuda.memory.reset_peak_memory_stats.html#torch.cuda.memory.reset_peak_memory_stats) | Reset the "peak" stats tracked by the CUDA memory allocator. |
| [`reset_peak_host_memory_stats`](generated/torch.cuda.memory.reset_peak_host_memory_stats.html#torch.cuda.memory.reset_peak_host_memory_stats) | Reset the "peak" stats tracked by the host memory allocator. |
| [`caching_allocator_alloc`](generated/torch.cuda.memory.caching_allocator_alloc.html#torch.cuda.memory.caching_allocator_alloc) | Perform a memory allocation using the CUDA memory allocator. |
| [`caching_allocator_delete`](generated/torch.cuda.memory.caching_allocator_delete.html#torch.cuda.memory.caching_allocator_delete) | Delete memory allocated using the CUDA memory allocator. |
| [`get_allocator_backend`](generated/torch.cuda.memory.get_allocator_backend.html#torch.cuda.memory.get_allocator_backend) | Return a string describing the active allocator backend as set by `PYTORCH_ALLOC_CONF`. |
| [`CUDAPluggableAllocator`](generated/torch.cuda.memory.CUDAPluggableAllocator.html#torch.cuda.memory.CUDAPluggableAllocator) | CUDA memory allocator loaded from a so file. |
| [`change_current_allocator`](generated/torch.cuda.memory.change_current_allocator.html#torch.cuda.memory.change_current_allocator) | Change the currently used memory allocator to be the one provided. |
| [`MemPool`](generated/torch.cuda.memory.MemPool.html#torch.cuda.memory.MemPool) | MemPool represents a pool of memory in a caching allocator. |

| [`caching_allocator_disabled`](generated/torch.cuda.memory.caching_allocator_disabled.html#torch.cuda.memory.caching_allocator_disabled) | Context manager that temporarily disables the CUDA caching allocator. |
| --- | --- |
| [`caching_allocator_enable`](generated/torch.cuda.memory.caching_allocator_enable.html#torch.cuda.memory.caching_allocator_enable) | Enable or disable the CUDA memory allocator. |

*class*torch.cuda.use_mem_pool(*pool*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/cuda/memory.py#L1320)

A context manager that routes allocations to a given pool.

Parameters:

- **pool** (*torch.cuda.MemPool*) - a MemPool object to be made active so that
allocations route to this pool.
- **device** ([*torch.device*](tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Uses MemPool on
the current device, given by [`current_device()`](generated/torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](generated/torch.cuda.device.html#torch.cuda.device) is `None` (default).

Note

This context manager makes only current thread's allocations route to
the given pool. If a new thread is spawned inside the context manager
(e.g. by calling backward) the allocations in that thread will not
route to the given pool.

torch.cuda.nccl.version()[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/cuda/nccl.py#L35)

Returns the version of the NCCL.

This function returns a tuple containing the major, minor, and patch version numbers of the NCCL.
The suffix is also included in the tuple if a version suffix exists.
:returns: The version information of the NCCL.
:rtype: tuple

| [`profile`](generated/torch.cuda.profiler.profile.html#torch.cuda.profiler.profile) | Enable profiling. |
| --- | --- |
| [`start`](generated/torch.cuda.profiler.start.html#torch.cuda.profiler.start) | Starts cuda profiler data collection. |
| [`stop`](generated/torch.cuda.profiler.stop.html#torch.cuda.profiler.stop) | Stops cuda profiler data collection. |

## NVIDIA Tools Extension (NVTX)

| [`nvtx.mark`](generated/torch.cuda.nvtx.mark.html#torch.cuda.nvtx.mark) | Describe an instantaneous event that occurred at some point. |
| --- | --- |
| [`nvtx.range_push`](generated/torch.cuda.nvtx.range_push.html#torch.cuda.nvtx.range_push) | Push a range onto a stack of nested range span. |
| [`nvtx.range_pop`](generated/torch.cuda.nvtx.range_pop.html#torch.cuda.nvtx.range_pop) | Pop a range off of a stack of nested range spans. |
| [`nvtx.range`](generated/torch.cuda.nvtx.range.html#torch.cuda.nvtx.range) | Context manager / decorator that pushes an NVTX range at the beginning of its scope, and pops it at the end. |
| [`nvtx.range_end`](generated/torch.cuda.nvtx.range_end.html#torch.cuda.nvtx.range_end) | Mark the end of a range for a given range_id. |
| [`nvtx.range_start`](generated/torch.cuda.nvtx.range_start.html#torch.cuda.nvtx.range_start) | Mark the start of a range with string message. |

## Jiterator (beta)

| [`jiterator._create_jit_fn`](generated/torch.cuda.jiterator._create_jit_fn.html#torch.cuda.jiterator._create_jit_fn) | Create a jiterator-generated cuda kernel for an elementwise op. |
| --- | --- |
| [`jiterator._create_multi_output_jit_fn`](generated/torch.cuda.jiterator._create_multi_output_jit_fn.html#torch.cuda.jiterator._create_multi_output_jit_fn) | Create a jiterator-generated cuda kernel for an elementwise op that supports returning one or more outputs. |

## TunableOp

Some operations could be implemented using more than one library or more than
one technique. For example, a GEMM could be implemented for CUDA or ROCm using
either the cublas/cublasLt libraries or hipblas/hipblasLt libraries,
respectively. How does one know which implementation is the fastest and should
be chosen? That's what TunableOp provides. Certain operators have been
implemented using multiple strategies as Tunable Operators. At runtime, all
strategies are profiled and the fastest is selected for all subsequent
operations.

See the [documentation](cuda.tunable.html) for information on how to use it.

## Stream Sanitizer (prototype)

CUDA Sanitizer is a prototype tool for detecting synchronization errors between streams in PyTorch.
See the [documentation](cuda._sanitizer.html) for information on how to use it.

## GPUDirect Storage (prototype)

The APIs in `torch.cuda.gds` provide thin wrappers around certain cuFile APIs that allow
direct memory access transfers between GPU memory and storage, avoiding a bounce buffer in the CPU. See the
[cufile api documentation](https://docs.nvidia.com/gpudirect-storage/api-reference-guide/index.html#cufile-io-api)
for more details.

These APIs can be used in versions greater than or equal to CUDA 12.6. In order to use these APIs, one must
ensure that their system is appropriately configured to use GPUDirect Storage per the
[GPUDirect Storage documentation](https://docs.nvidia.com/gpudirect-storage/troubleshooting-guide/contents.html).

See the docs for [`GdsFile`](generated/torch.cuda.gds.GdsFile.html#torch.cuda.gds.GdsFile) for an example of how to use these.

| [`gds_register_buffer`](generated/torch.cuda.gds.gds_register_buffer.html#torch.cuda.gds.gds_register_buffer) | Registers a storage on a CUDA device as a cufile buffer. |
| --- | --- |
| [`gds_deregister_buffer`](generated/torch.cuda.gds.gds_deregister_buffer.html#torch.cuda.gds.gds_deregister_buffer) | Deregisters a previously registered storage on a CUDA device as a cufile buffer. |
| [`GdsFile`](generated/torch.cuda.gds.GdsFile.html#torch.cuda.gds.GdsFile) | Wrapper around cuFile. |

## Green Contexts (experimental)

`torch.cuda.green_contexts` provides thin wrappers around the CUDA Green Context APIs
to enable more general carveout of SM resources for CUDA kernels.

These APIs can be used in PyTorch with CUDA versions greater than or equal to 12.8.

See the docs for [`GreenContext`](generated/torch.cuda.green_contexts.GreenContext.html#torch.cuda.green_contexts.GreenContext) for an example of how to use these.

| [`GreenContext`](generated/torch.cuda.green_contexts.GreenContext.html#torch.cuda.green_contexts.GreenContext) | Wrapper around a CUDA green context. |
| --- | --- |

torch.cuda.nccl.is_available(*tensors*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/cuda/nccl.py#L14)

This package adds support for NVIDIA Tools Extension (NVTX) used in profiling.