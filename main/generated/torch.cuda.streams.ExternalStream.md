# ExternalStream

*class*torch.cuda.streams.ExternalStream(*stream_ptr*, *device=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/cuda/streams.py#L136)

Wrapper around an externally allocated CUDA stream.

This class is used to wrap streams allocated in other libraries in order
to facilitate data exchange and multi-library interactions.

Note

This class doesn't manage the stream life-cycle, it is the user
responsibility to keep the referenced stream alive while this class is
being used.

Parameters:

- **stream_ptr** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Integer representation of the cudaStream_t value.
allocated externally.
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the device where the stream
was originally allocated. If device is specified incorrectly,
subsequent launches using this stream may fail.

query()[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/cuda/streams.py#L94)

Check if all the work submitted has been completed.

Returns:

A boolean indicating if all kernels in this stream are completed.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

record_event(*event=None*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/cuda/streams.py#L79)

Record an event.

Parameters:

**event** ([*Event*](torch.cuda.streams.Event.html#torch.cuda.streams.Event)*,*[*torch.Event*](torch.Event.html#torch.Event)*,**optional*) - event to record. If not given, a new one
will be allocated.

Returns:

Recorded event.

synchronize()[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/cuda/streams.py#L102)

Wait for all the kernels in this stream to complete.

Note

This is a wrapper around `cudaStreamSynchronize()`: see
[CUDA Stream documentation](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html) for more info.

wait_event(*event*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/cuda/streams.py#L48)

Make all future work submitted to the stream wait for an event.

Parameters:

**event** ([*Event*](torch.cuda.streams.Event.html#torch.cuda.streams.Event)*,*[*torch.Event*](torch.Event.html#torch.Event)) - an event to wait for.

Note

This is a wrapper around `cudaStreamWaitEvent()`: see
[CUDA Stream documentation](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html) for more info.

This function returns without waiting for `event`: only future
operations are affected.

wait_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/cuda/streams.py#L65)

Synchronize with another stream.

All future work submitted to this stream will wait until all kernels
submitted to a given stream at the time of call complete.

Parameters:

**stream** ([*Stream*](torch.cuda.streams.Stream.html#torch.cuda.streams.Stream)*,*[*torch.Stream*](torch.Stream.html#torch.Stream)) - a stream to synchronize.

Note

This function returns without waiting for currently enqueued
kernels in `stream`: only future operations are affected.