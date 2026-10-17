# Event

*class*torch.mps.event.Event(*enable_timing=False*)[[source]](https://github.com/pytorch/pytorch/blob/64cf21712548b5b1ea993d13784345169fb72869/torch/mps/event.py#L11)

Wrapper around an MPS event.

MPS events are synchronization markers that can be used to monitor the
device's progress, to accurately measure timing, and to synchronize MPS streams.

Parameters:

**enable_timing** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - indicates if the event should measure time
(default: `False`)

elapsed_time(*end_event*)[[source]](https://github.com/pytorch/pytorch/blob/64cf21712548b5b1ea993d13784345169fb72869/torch/mps/event.py#L64)

Returns the time elapsed in milliseconds after the event was
recorded and before the end_event was recorded.

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float)

query()[[source]](https://github.com/pytorch/pytorch/blob/64cf21712548b5b1ea993d13784345169fb72869/torch/mps/event.py#L54)

Returns True if all work currently captured by event has completed.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)

record(*stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/64cf21712548b5b1ea993d13784345169fb72869/torch/mps/event.py#L30)

Records the event in a given stream.

Parameters:

**stream** (*torch.mps.Stream**,*[*torch.Stream*](torch.Stream.html#torch.Stream)*,**optional*) - Uses `torch.mps.current_stream()` if no stream is specified.

synchronize()[[source]](https://github.com/pytorch/pytorch/blob/64cf21712548b5b1ea993d13784345169fb72869/torch/mps/event.py#L58)

Waits until the completion of all work currently captured in this event.
This prevents the CPU thread from proceeding until the event completes.

wait(*stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/64cf21712548b5b1ea993d13784345169fb72869/torch/mps/event.py#L42)

Makes all future work submitted to the given stream wait for this event.

Parameters:

**stream** (*torch.mps.Stream**,*[*torch.Stream*](torch.Stream.html#torch.Stream)*,**optional*) - Uses `torch.mps.current_stream()` if no stream is specified.