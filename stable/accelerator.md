# torch.accelerator

## Lazy Initialization and Fork Safety

Accelerator runtimes (CUDA, XPU, MPS, etc.) are initialized lazily -- only
when the first operation that touches the device runs. This ensures that
`import torch` and capability queries do not poison subsequent `fork()`
calls. See [Poison fork in multiprocessing](notes/multiprocessing.html#multiprocessing-poison-fork-note) for background.

Certain APIs need to be callable before forking (e.g., `device_count()`,
`is_available()`), and some backends provide opt-in mechanisms to make
these fork-safe (e.g., CUDA via NVML, XPU via Level Zero Sysman). To keep
behavior and runtime state consistent between `torch.accelerator` and
per-backend modules, the following APIs are delegated to each backend:

- **`is_available()` / `device_count()`** should ideally answer without
bringing up the runtime, since `DataLoader` and similar tools rely on
calling them before forking. Whether this is achievable depends on the
backend, so `torch.accelerator` forwards to the corresponding backend
implementation.
- **`_lazy_call()`** is used for deferred RNG management. Calling
`manual_seed()` before forking should not force runtime initialization.
`torch.accelerator` wraps the seeding callback via `_lazy_call()`, which
forwards to the backend's own callback queue (CUDA, XPU, MTIA, ...).
Each backend owns its init flag and callback queue. If a backend does not
provide `_lazy_call` (e.g., MPS), the callback executes immediately.

This package introduces support for the current [accelerator](torch.html#accelerators) in python.

| [`device_count`](generated/torch.accelerator.device_count.html#torch.accelerator.device_count) | Return the number of current [accelerator](torch.html#accelerators) available. |
| --- | --- |
| [`is_available`](generated/torch.accelerator.is_available.html#torch.accelerator.is_available) | Check if the current accelerator is available at runtime: it was built, all the required drivers are available and at least one device is visible. |
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

## Random Number Generator

| [`get_rng_state`](generated/torch.accelerator.random.get_rng_state.html#torch.accelerator.random.get_rng_state) | Return the RNG state of the default [`torch.Generator`](generated/torch.Generator.html#torch.Generator) for the current [accelerator](torch.html#accelerators) as a torch.Tensor of dtype torch.uint8 for the specified accelerator device. |
| --- | --- |
| [`get_rng_state_all`](generated/torch.accelerator.random.get_rng_state_all.html#torch.accelerator.random.get_rng_state_all) | Return a list of torch.Tensor of dtype torch.uint8 representing the RNG states of all devices for the current [accelerator](torch.html#accelerators). |
| [`initial_seed`](generated/torch.accelerator.random.initial_seed.html#torch.accelerator.random.initial_seed) | Return the initial seed of the default [`torch.Generator`](generated/torch.Generator.html#torch.Generator) for the current [accelerator](torch.html#accelerators) on the specified device. |