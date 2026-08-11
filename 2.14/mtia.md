# torch.mtia

The MTIA backend is implemented out of the tree, only interfaces are defined
here.

This package enables an interface for accessing MTIA backend in python

| [`StreamContext`](generated/torch.mtia.StreamContext.html#torch.mtia.StreamContext) | Context-manager that selects a given stream. |
| --- | --- |
| [`current_device`](generated/torch.mtia.current_device.html#torch.mtia.current_device) | Return the index of a currently selected device. |
| [`current_stream`](generated/torch.mtia.current_stream.html#torch.mtia.current_stream) | Return the currently selected [`Stream`](generated/torch.mtia.Stream_class.html#torch.mtia.Stream) for a given device. |
| [`default_stream`](generated/torch.mtia.default_stream.html#torch.mtia.default_stream) | Return the default [`Stream`](generated/torch.mtia.Stream_class.html#torch.mtia.Stream) for a given device. |
| [`device_count`](generated/torch.mtia.device_count.html#torch.mtia.device_count) | Return the number of MTIA devices available. |
| [`init`](generated/torch.mtia.init.html#torch.mtia.init) | |
| [`is_available`](generated/torch.mtia.is_available.html#torch.mtia.is_available) | Return true if MTIA device is available |
| [`is_bf16_supported`](generated/torch.mtia.is_bf16_supported.html#torch.mtia.is_bf16_supported) | Return a bool indicating if the current MTIA device supports dtype bfloat16. |
| [`is_initialized`](generated/torch.mtia.is_initialized.html#torch.mtia.is_initialized) | Return whether PyTorch's MTIA state has been initialized. |
| [`memory_stats`](generated/torch.mtia.memory_stats.html#torch.mtia.memory_stats) | Return a dictionary of MTIA memory allocator statistics for a given device. |
| [`get_device_capability`](generated/torch.mtia.get_device_capability.html#torch.mtia.get_device_capability) | Return capability of a given device as a tuple of (major version, minor version). |
| [`get_device_properties`](generated/torch.mtia.get_device_properties.html#torch.mtia.get_device_properties) | Return a dictionary of MTIA device properties |
| [`empty_cache`](generated/torch.mtia.empty_cache.html#torch.mtia.empty_cache) | Empty the MTIA device cache. |
| [`record_memory_history`](generated/torch.mtia.record_memory_history.html#torch.mtia.record_memory_history) | Enable/Disable the memory profiler on MTIA allocator |
| [`snapshot`](generated/torch.mtia.snapshot.html#torch.mtia.snapshot) | Return a dictionary of MTIA memory allocator history |
| [`attach_out_of_memory_observer`](generated/torch.mtia.attach_out_of_memory_observer.html#torch.mtia.attach_out_of_memory_observer) | Attach an out-of-memory observer to MTIA memory allocator |
| [`set_device`](generated/torch.mtia.set_device.html#torch.mtia.set_device) | Set the current device. |
| [`set_stream`](generated/torch.mtia.set_stream.html#torch.mtia.set_stream) | Set the current stream. This is a wrapper API to set the stream. |
| [`stream`](generated/torch.mtia.stream_function.html#torch.mtia.stream) | Wrap around the Context-manager StreamContext that selects a given stream. |
| [`synchronize`](generated/torch.mtia.synchronize.html#torch.mtia.synchronize) | Waits for all jobs in all streams on a MTIA device to complete. |
| [`device`](generated/torch.mtia.device.html#torch.mtia.device) | Context-manager that changes the selected device. |
| [`set_rng_state`](generated/torch.mtia.set_rng_state.html#torch.mtia.set_rng_state) | Sets the random number generator state of the specified MTIA device. |
| [`get_rng_state`](generated/torch.mtia.get_rng_state.html#torch.mtia.get_rng_state) | Returns the random number generator state of the specified MTIA device as a ByteTensor. |
| [`set_rng_state_all`](generated/torch.mtia.set_rng_state_all.html#torch.mtia.set_rng_state_all) | Sets the random number generator state of all devices. |
| [`get_rng_state_all`](generated/torch.mtia.get_rng_state_all.html#torch.mtia.get_rng_state_all) | Returns a list of ByteTensor representing the random number states of all devices. |
| [`manual_seed`](generated/torch.mtia.manual_seed.html#torch.mtia.manual_seed) | Sets the seed for generating random numbers for the current MTIA device. |
| [`manual_seed_all`](generated/torch.mtia.manual_seed_all.html#torch.mtia.manual_seed_all) | Sets the seed for generating random numbers on all MTIA devices. |
| [`seed`](generated/torch.mtia.seed.html#torch.mtia.seed) | Sets the seed for generating random numbers to a random number for the current MTIA device. |
| [`seed_all`](generated/torch.mtia.seed_all.html#torch.mtia.seed_all) | Sets the seed for generating random numbers to a random number on all MTIA devices. |
| [`initial_seed`](generated/torch.mtia.initial_seed.html#torch.mtia.initial_seed) | Returns the current random seed of the current MTIA device. |
| [`DeferredMtiaCallError`](generated/torch.mtia.DeferredMtiaCallError.html#torch.mtia.DeferredMtiaCallError) | |

## Streams and events

| [`Event`](generated/torch.mtia.Event.html#torch.mtia.Event) | Query and record Stream status to identify or control dependencies across Stream and measure timing. |
| --- | --- |
| [`Stream`](generated/torch.mtia.Stream_class.html#torch.mtia.Stream) | An in-order queue of executing the respective tasks asynchronously in first in first out (FIFO) order. |