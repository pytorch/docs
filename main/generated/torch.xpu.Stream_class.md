# Stream

*class*torch.xpu.Stream(*device=None*, *priority=0*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/xpu/streams.py#L17)

Wrapper around a XPU stream.

A XPU stream is a linear sequence of execution that belongs to a specific
device, independent from other streams. It supports with statement as a
context manager to ensure the operators within the with block are running
on the corresponding stream.

Parameters:

- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - a device on which to allocate
the stream. If [`device`](torch.xpu.device.html#torch.xpu.device) is `None` (default) or a negative
integer, this will use the current device.
- **priority** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - priority of the stream, which can be positive, 0, or negative.
A lower number indicates a higher priority. By default, the priority is set to 0.
If the value falls outside of the allowed priority range, it will automatically be
mapped to the nearest valid priority (lowest for large positive numbers or
highest for large negative numbers).

query()[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/xpu/streams.py#L78)

Check if all the work submitted has been completed.

Returns:

A boolean indicating if all kernels in this stream are completed.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

record_event(*event=None*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/xpu/streams.py#L63)

Record an event.

Parameters:

**event** ([*Event*](torch.xpu.Event.html#torch.xpu.Event)*,*[*torch.Event*](torch.Event.html#torch.Event)*,**optional*) - event to record. If not given, a new one
will be allocated.

Returns:

Recorded event.

synchronize()[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/xpu/streams.py#L86)

Wait for all the kernels in this stream to complete.

wait_event(*event*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/xpu/streams.py#L44)

Make all future work submitted to the stream wait for an event.

Parameters:

**event** ([*Event*](torch.xpu.Event.html#torch.xpu.Event)*,*[*torch.Event*](torch.Event.html#torch.Event)) - an event to wait for.

wait_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/xpu/streams.py#L52)

Synchronize with another stream.

All future work submitted to this stream will wait until all kernels
submitted to a given stream at the time of call complete.

Parameters:

**stream** (*Stream**,*[*torch.Stream*](torch.Stream.html#torch.Stream)) - a stream to synchronize.