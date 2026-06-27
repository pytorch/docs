# Event

*class*torch.xpu.streams.Event(*enable_timing=False*)[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/xpu/streams.py#L106)

Wrapper around a XPU event.

XPU events are synchronization markers that can be used to monitor the
device's progress, and to synchronize XPU streams.

The underlying XPU events are lazily initialized when the event is first
recorded. After creation, only streams on the same device may record the
event. However, streams on any device can wait on the event.

Parameters:

**enable_timing** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - indicates if the event should measure time
(default: `False`)

elapsed_time(*end_event*)[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/xpu/streams.py#L154)

Return the time elapsed.

Time reported in milliseconds after the event was recorded and
before the end_event was recorded.

Parameters:

**end_event** (*Event*) - the end event.

query()[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/xpu/streams.py#L145)

Check if all work currently captured by event has completed.

Returns:

A boolean indicating if all work currently captured by event has
completed.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

record(*stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/xpu/streams.py#L124)

Record the event in a given stream.

Parameters:

**stream** ([*Stream*](torch.xpu.streams.Stream.html#torch.xpu.streams.Stream)*,*[*torch.Stream*](torch.Stream.html#torch.Stream)*,**optional*) - Uses `torch.xpu.current_stream()` if no stream is specified.
The stream's device must match the event's device.

synchronize()[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/xpu/streams.py#L165)

Wait for the event to complete.

Waits until the completion of all work currently captured in this event.
This prevents the CPU thread from proceeding until the event completes.

wait(*stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/xpu/streams.py#L135)

Make all future work submitted to the given stream wait for this event.

Parameters:

**stream** ([*Stream*](torch.xpu.streams.Stream.html#torch.xpu.streams.Stream)*,*[*torch.Stream*](torch.Stream.html#torch.Stream)*,**optional*) - Uses `torch.xpu.current_stream()` if no stream is specified.