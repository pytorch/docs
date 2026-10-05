# torch.cpu

This package implements abstractions found in `torch.cuda`
to facilitate writing device-agnostic code.

| [`current_device`](generated/torch.cpu.current_device.html#torch.cpu.current_device) | Returns current device for cpu. |
| --- | --- |
| [`current_stream`](generated/torch.cpu.current_stream.html#torch.cpu.current_stream) | Returns the currently selected [`Stream`](generated/torch.cpu.Stream_class.html#torch.cpu.Stream) for a given device. |
| [`get_capabilities`](generated/torch.cpu.get_capabilities.html#torch.cpu.get_capabilities) | Returns an immutable mapping of CPU capabilities detected at runtime. |
| [`is_available`](generated/torch.cpu.is_available.html#torch.cpu.is_available) | Returns a bool indicating if CPU is currently available. |
| [`is_initialized`](generated/torch.cpu.is_initialized.html#torch.cpu.is_initialized) | Returns True if the CPU is initialized. |
| [`synchronize`](generated/torch.cpu.synchronize.html#torch.cpu.synchronize) | Waits for all kernels in all streams on the CPU device to complete. |
| [`stream`](generated/torch.cpu.stream_function.html#torch.cpu.stream) | Wrapper around the Context-manager StreamContext that selects a given stream. |
| [`set_device`](generated/torch.cpu.set_device.html#torch.cpu.set_device) | Sets the current device, in CPU we do nothing. |
| [`device_count`](generated/torch.cpu.device_count.html#torch.cpu.device_count) | Returns number of CPU devices (not cores). |
| [`StreamContext`](generated/torch.cpu.StreamContext.html#torch.cpu.StreamContext) | Context-manager that selects a given stream. |

## Streams and events

| [`Stream`](generated/torch.cpu.Stream_class.html#torch.cpu.Stream) | N.B. |
| --- | --- |