# Stream

*class*torch.mps.Stream(*device=None*, ***kwargs*)

Wrapper around an MPS stream.

An MPS stream is a linear sequence of execution that is independent from
other streams. Use the [`stream()`](torch.mps.stream_function.html#torch.mps.stream) context manager to ensure operators
run on the corresponding stream.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - a device on which to allocate
the stream. If `device` is `None` (default) or a negative
integer, this will use the current device.

synchronize()[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/mps/streams.py#L46)

Wait for all the kernels in this stream to complete.