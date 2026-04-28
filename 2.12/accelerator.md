# torch.accelerator

This package introduces support for the current [accelerator](torch.html#accelerators) in python.

| [`device_count`](generated/torch.accelerator.device_count.html#torch.accelerator.device_count) | Return the number of current [accelerator](torch.html#accelerators) available. |
| --- | --- |
| [`is_available`](generated/torch.accelerator.is_available.html#torch.accelerator.is_available) | Check if the current accelerator is available at runtime: it was build, all the required drivers are available and at least one device is visible. |
| [`current_accelerator`](generated/torch.accelerator.current_accelerator.html#torch.accelerator.current_accelerator) | Return the device of the accelerator available at compilation time. |
| [`set_device_index`](generated/torch.accelerator.set_device_index.html#torch.accelerator.set_device_index) | Set the current device index to a given device. |
| [`set_device_idx`](generated/torch.accelerator.set_device_idx.html#torch.accelerator.set_device_idx) | (Deprecated) Set the current device index to a given device. |
| [`current_device_index`](generated/torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) | Return the index of a currently selected device for the current [accelerator](torch.html#accelerators). |
| [`current_device_idx`](generated/torch.accelerator.current_device_idx.html#torch.accelerator.current_device_idx) | (Deprecated) Return the index of a currently selected device for the current [accelerator](torch.html#accelerators). |
| [`get_device_capability`](generated/torch.accelerator.get_device_capability.html#torch.accelerator.get_device_capability) | Return the capability of the currently selected device. |
| [`set_stream`](generated/torch.accelerator.set_stream.html#torch.accelerator.set_stream) | Set the current stream to a given stream. |
| [`current_stream`](generated/torch.accelerator.current_stream.html#torch.accelerator.current_stream) | Return the currently selected stream for a given device. |
| [`synchronize`](generated/torch.accelerator.synchronize.html#torch.accelerator.synchronize) | Wait for all kernels in all streams on the given device to complete. |
| [`device_index`](generated/torch.accelerator.device_index.html#torch.accelerator.device_index) | Context manager to set the current device index for the current [accelerator](torch.html#accelerators). |

## Graphs

| [`Graph`](generated/torch.accelerator.Graph.html#torch.accelerator.Graph) | Wrapper around an [accelerator](torch.html#accelerators) graph that supports capture and replay. |
| --- | --- |

## Memory management

| [`empty_cache`](generated/torch.accelerator.memory.empty_cache.html#torch.accelerator.memory.empty_cache) | Release all unoccupied cached memory currently held by the caching allocator so that those can be used in other application. |
| --- | --- |
| [`empty_host_cache`](generated/torch.accelerator.memory.empty_host_cache.html#torch.accelerator.memory.empty_host_cache) | Release all unoccupied cached host (pinned) memory currently held by the host caching allocator so that it can be used by other applications. |
| [`get_memory_info`](generated/torch.accelerator.memory.get_memory_info.html#torch.accelerator.memory.get_memory_info) | Return the current device memory information for a given device index. |
| [`max_memory_allocated`](generated/torch.accelerator.memory.max_memory_allocated.html#torch.accelerator.memory.max_memory_allocated) | Return the current [accelerator](torch.html#accelerators) maximum device memory occupied by tensors in bytes for a given device index. |
| [`max_memory_reserved`](generated/torch.accelerator.memory.max_memory_reserved.html#torch.accelerator.memory.max_memory_reserved) | Return the current [accelerator](torch.html#accelerators) maximum device memory managed by the caching allocator in bytes for a given device index. |
| [`memory_allocated`](generated/torch.accelerator.memory.memory_allocated.html#torch.accelerator.memory.memory_allocated) | Return the current [accelerator](torch.html#accelerators) device memory occupied by tensors in bytes for a given device index. |
| [`memory_reserved`](generated/torch.accelerator.memory.memory_reserved.html#torch.accelerator.memory.memory_reserved) | Return the current [accelerator](torch.html#accelerators) device memory managed by the caching allocator in bytes for a given device index. |
| [`memory_stats`](generated/torch.accelerator.memory.memory_stats.html#torch.accelerator.memory.memory_stats) | Return a dictionary of accelerator device memory allocator statistics for a given device index. |
| [`reset_accumulated_memory_stats`](generated/torch.accelerator.memory.reset_accumulated_memory_stats.html#torch.accelerator.memory.reset_accumulated_memory_stats) | Reset the "accumulated" (historical) stats tracked by the current [accelerator](torch.html#accelerators) memory allocator for a given device index. |
| [`reset_peak_memory_stats`](generated/torch.accelerator.memory.reset_peak_memory_stats.html#torch.accelerator.memory.reset_peak_memory_stats) | Reset the "peak" stats tracked by the current [accelerator](torch.html#accelerators) memory allocator for a given device index. |