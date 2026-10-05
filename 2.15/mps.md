# torch.mps

This package enables an interface for accessing MPS (Metal Performance Shaders) backend in Python.
Metal is Apple's API for programming metal GPU (graphics processor unit). Using MPS means that increased
performance can be achieved, by running work on the metal GPU(s).
See [https://developer.apple.com/documentation/metalperformanceshaders](https://developer.apple.com/documentation/metalperformanceshaders) for more details.

| [`is_available`](generated/torch.mps.is_available.html#torch.mps.is_available) | |
| --- | --- |
| [`device_count`](generated/torch.mps.device_count.html#torch.mps.device_count) | Returns the number of available MPS devices. |
| [`synchronize`](generated/torch.mps.synchronize.html#torch.mps.synchronize) | Waits for all kernels in all streams on a MPS device to complete. |
| [`get_rng_state`](generated/torch.mps.get_rng_state.html#torch.mps.get_rng_state) | Returns the random number generator state as a ByteTensor. |
| [`set_rng_state`](generated/torch.mps.set_rng_state.html#torch.mps.set_rng_state) | Sets the random number generator state. |
| [`manual_seed`](generated/torch.mps.manual_seed.html#torch.mps.manual_seed) | Sets the seed for generating random numbers. |
| [`seed`](generated/torch.mps.seed.html#torch.mps.seed) | Sets the seed for generating random numbers to a random number. |
| [`empty_cache`](generated/torch.mps.empty_cache.html#torch.mps.empty_cache) | Releases all unoccupied cached memory currently held by the caching allocator so that those can be used in other GPU applications. |
| [`set_per_process_memory_fraction`](generated/torch.mps.set_per_process_memory_fraction.html#torch.mps.set_per_process_memory_fraction) | Set memory fraction for limiting process's memory allocation on MPS device. |
| [`current_allocated_memory`](generated/torch.mps.current_allocated_memory.html#torch.mps.current_allocated_memory) | Returns the current GPU memory occupied by tensors in bytes. |
| [`driver_allocated_memory`](generated/torch.mps.driver_allocated_memory.html#torch.mps.driver_allocated_memory) | Returns total GPU memory allocated by Metal driver for the process in bytes. |
| [`recommended_max_memory`](generated/torch.mps.recommended_max_memory.html#torch.mps.recommended_max_memory) | Returns recommended max Working set size for GPU memory in bytes. |
| [`compile_shader`](generated/torch.mps.compile_shader.html#torch.mps.compile_shader) | Compiles compute shader from source and allows one to invoke kernels defined there from the comfort of Python runtime Example. |
| [`load_metallib`](generated/torch.mps.load_metallib.html#torch.mps.load_metallib) | Loads a precompiled Metal library (.metallib) and returns a shader library object that allows invoking kernels defined in it. |

## MPS Profiler

| [`profiler.start`](generated/torch.mps.profiler.start.html#torch.mps.profiler.start) | Start OS Signpost tracing from MPS backend. |
| --- | --- |
| [`profiler.stop`](generated/torch.mps.profiler.stop.html#torch.mps.profiler.stop) | Stops generating OS Signpost tracing from MPS backend. |
| [`profiler.profile`](generated/torch.mps.profiler.profile.html#torch.mps.profiler.profile) | Context Manager to enabling generating OS Signpost tracing from MPS backend. |
| [`profiler.is_capturing_metal`](generated/torch.mps.profiler.is_capturing_metal.html#torch.mps.profiler.is_capturing_metal) | Checks if metal capture is in progress |
| [`profiler.is_metal_capture_enabled`](generated/torch.mps.profiler.is_metal_capture_enabled.html#torch.mps.profiler.is_metal_capture_enabled) | Checks if metal_capture context manager is usable To enable metal capture, set MTL_CAPTURE_ENABLED envvar |
| [`profiler.metal_capture`](generated/torch.mps.profiler.metal_capture.html#torch.mps.profiler.metal_capture) | Context manager that enables capturing of Metal calls into gputrace |

## MPS Event

| [`event.Event`](generated/torch.mps.event.Event.html#torch.mps.event.Event) | Wrapper around an MPS event. |
| --- | --- |