# Event

*class*torch.cuda.streams.Event(*enable_timing=False*, *blocking=False*, *interprocess=False*, *external=False*)[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/cuda/streams.py#L159)

Wrapper around a CUDA event.

CUDA events are synchronization markers that can be used to monitor the
device's progress, to accurately measure timing, and to synchronize CUDA
streams.

The underlying CUDA events are lazily initialized when the event is first
recorded or exported to another process. After creation, only streams on the
same device may record the event. However, streams on any device can wait on
the event.

Parameters:

- **enable_timing** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - indicates if the event should measure time
(default: `False`)
- **blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True`, `wait()` will be blocking (default: `False`)
- **interprocess** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, the event can be shared between processes
(default: `False`)
- **external** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - indicates whether this event should create event record and event wait nodes, or create an internal cross-stream dependency, when captured in a cuda graph. See [cross-stream dependencies](https://docs.nvidia.com/cuda/archive/12.9.0/cuda-c-programming-guide/index.html#cross-stream-dependencies-and-events), [cudaEventRecordExternal](https://docs.nvidia.com/cuda/archive/12.9.0/cuda-runtime-api/group__CUDART__TYPES.html#group__CUDART__TYPES_1g3457b81d1d32c6a00f6132fbc2693d47), and [cudaEventWaitExternal](https://docs.nvidia.com/cuda/archive/12.9.0/cuda-runtime-api/group__CUDART__TYPES.html#group__CUDART__TYPES_1g0c23426b7252eaa9cef695859991304e) for more information about internal vs. external events. (default: `False`)

elapsed_time(*end_event*)[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/cuda/streams.py#L234)

Return the time elapsed.

Time reported in milliseconds after the event was recorded and
before the end_event was recorded.

Parameters:

**end_event** (*Event*) - the end event.

*classmethod*from_ipc_handle(*device*, *handle*)[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/cuda/streams.py#L194)

Reconstruct an event from an IPC handle on the given device.

ipc_handle()[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/cuda/streams.py#L256)

Return an IPC handle of this event.

If not recorded yet, the event will use the current device.

query()[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/cuda/streams.py#L225)

Check if all work currently captured by event has completed.

Returns:

A boolean indicating if all work currently captured by event has
completed.

record(*stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/cuda/streams.py#L199)

Record the event in a given stream.

Parameters:

**stream** ([*Stream*](torch.cuda.streams.Stream.html#torch.cuda.streams.Stream)*,*[*torch.Stream*](torch.Stream.html#torch.Stream)*,**optional*) - Uses `torch.cuda.current_stream()` if no stream is specified.
The stream's device must match the event's device.

synchronize()[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/cuda/streams.py#L245)

Wait for the event to complete.

Waits until the completion of all work currently captured in this event.
This prevents the CPU thread from proceeding until the event completes.

> Note
> 
> 
> 
> 
> This is a wrapper around `cudaEventSynchronize()`: see
> [CUDA Event documentation](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__EVENT.html) for more info.

wait(*stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/cuda/streams.py#L211)

Make all future work submitted to the given stream wait for this event.

Parameters:

**stream** ([*Stream*](torch.cuda.streams.Stream.html#torch.cuda.streams.Stream)*,*[*torch.Stream*](torch.Stream.html#torch.Stream)*,**optional*) - Uses `torch.cuda.current_stream()` if no stream is specified.

Note

This is a wrapper around `cudaStreamWaitEvent()`: see
[CUDA Event documentation](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__EVENT.html) for more info.