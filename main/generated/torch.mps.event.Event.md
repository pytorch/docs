# Event

*class*torch.mps.event.Event(*enable_timing=False*)[[source]](https://github.com/pytorch/pytorch/blob/496340f06ef7bda2800522429ba3f4e3473a92fa/torch/mps/event.py#L4)

Wrapper around an MPS event.

MPS events are synchronization markers that can be used to monitor the
device's progress, to accurately measure timing, and to synchronize MPS streams.

Parameters:

**enable_timing** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - indicates if the event should measure time
(default: `False`)

elapsed_time(*end_event*)[[source]](https://github.com/pytorch/pytorch/blob/496340f06ef7bda2800522429ba3f4e3473a92fa/torch/mps/event.py#L45)

Returns the time elapsed in milliseconds after the event was
recorded and before the end_event was recorded.

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float)

query()[[source]](https://github.com/pytorch/pytorch/blob/496340f06ef7bda2800522429ba3f4e3473a92fa/torch/mps/event.py#L35)

Returns True if all work currently captured by event has completed.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)

record()[[source]](https://github.com/pytorch/pytorch/blob/496340f06ef7bda2800522429ba3f4e3473a92fa/torch/mps/event.py#L23)

Records the event in the current stream.

synchronize()[[source]](https://github.com/pytorch/pytorch/blob/496340f06ef7bda2800522429ba3f4e3473a92fa/torch/mps/event.py#L39)

Waits until the completion of all work currently captured in this event.
This prevents the CPU thread from proceeding until the event completes.

wait()[[source]](https://github.com/pytorch/pytorch/blob/496340f06ef7bda2800522429ba3f4e3473a92fa/torch/mps/event.py#L29)

Makes all future work submitted to the current stream wait for this event.