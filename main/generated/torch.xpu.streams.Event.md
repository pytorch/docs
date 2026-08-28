# Event

*class*torch.xpu.streams.Event(*enable_timing=False*, *blocking=False*, *interprocess=False*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/xpu/streams.py#L106)

Wrapper around a XPU event.

XPU events are synchronization markers that can be used to monitor the
device's progress, and to synchronize XPU streams.

The underlying XPU events are lazily initialized when the event is first
recorded. After creation, only streams on the same device may record the
event. However, streams on any device can wait on the event.

Parameters:

- **enable_timing** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - indicates if the event should measure time
(default: `False`)
- **blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - unused and reserved (default: `False`)
- **interprocess** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - indicates if the event should be shareable
between processes (default: `False`)

elapsed_time(*end_event*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/xpu/streams.py#L159)

Return the time elapsed.

Time reported in milliseconds after the event was recorded and
before the end_event was recorded.

Parameters:

**end_event** (*Event*) - the end event.

*classmethod*from_ipc_handle(*device*, *ipc_handle*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/xpu/streams.py#L192)

Reconstruct an event from an IPC handle on the given device.

Parameters:

- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*, or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - the device on which to open the handle.
- **ipc_handle** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)) - the IPC handle returned by `ipc_handle()`.

Returns:

an event reconstructed from the IPC handle.

Return type:

Event

ipc_handle()[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/xpu/streams.py#L178)

Return an IPC handle of this event.

The event must have been constructed with `interprocess=True`.
If not yet recorded, the event is eagerly initialized on the current device.

Note

The event reconstructed with `from_ipc_handle()` cannot be re-exported via `ipc_handle()`.

Returns:

an opaque byte string that can be passed to `from_ipc_handle()`

in another process to reconstruct this event.

Return type:

[bytes](https://docs.python.org/3/library/stdtypes.html#bytes)

query()[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/xpu/streams.py#L150)

Check if all work currently captured by event has completed.

Returns:

A boolean indicating if all work currently captured by event has
completed.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

record(*stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/xpu/streams.py#L129)

Record the event in a given stream.

Parameters:

**stream** ([*Stream*](torch.xpu.streams.Stream.html#torch.xpu.streams.Stream)*,*[*torch.Stream*](torch.Stream.html#torch.Stream)*,**optional*) - Uses `torch.xpu.current_stream()` if no stream is specified.
The stream's device must match the event's device.

synchronize()[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/xpu/streams.py#L170)

Wait for the event to complete.

Waits until the completion of all work currently captured in this event.
This prevents the CPU thread from proceeding until the event completes.

wait(*stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/xpu/streams.py#L140)

Make all future work submitted to the given stream wait for this event.

Parameters:

**stream** ([*Stream*](torch.xpu.streams.Stream.html#torch.xpu.streams.Stream)*,*[*torch.Stream*](torch.Stream.html#torch.Stream)*,**optional*) - Uses `torch.xpu.current_stream()` if no stream is specified.