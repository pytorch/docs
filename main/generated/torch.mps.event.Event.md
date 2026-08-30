# Event

*class*torch.mps.event.Event(*enable_timing=False*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/mps/event.py#L4)

Wrapper around an MPS event.

MPS events are synchronization markers that can be used to monitor the
device's progress, to accurately measure timing, and to synchronize MPS streams.

Parameters:

**enable_timing** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - indicates if the event should measure time
(default: `False`)

elapsed_time(*end_event*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/mps/event.py#L41)

Returns the time elapsed in milliseconds after the event was
recorded and before the end_event was recorded.

Return type:

[float](https://docs.python.org/3/library/functions.html#float)

query()[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/mps/event.py#L31)

Returns True if all work currently captured by event has completed.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

record()[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/mps/event.py#L23)

Records the event in the default stream.

synchronize()[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/mps/event.py#L35)

Waits until the completion of all work currently captured in this event.
This prevents the CPU thread from proceeding until the event completes.

wait()[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/mps/event.py#L27)

Makes all future work submitted to the default stream wait for this event.