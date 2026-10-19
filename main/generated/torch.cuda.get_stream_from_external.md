# torch.cuda.get_stream_from_external

torch.cuda.get_stream_from_external(*data_ptr*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/__init__.py#L1423)

Return a [`Stream`](torch.cuda.Stream_class.html#torch.cuda.Stream) from an externally allocated CUDA stream.

This function is used to wrap streams allocated in other libraries in order
to facilitate data exchange and multi-library interactions.

Note

This function doesn't manage the stream life-cycle, it is the user
responsibility to keep the referenced stream alive while this returned
stream is being used.

Parameters:

- **data_ptr** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Integer representation of the cudaStream_t value that
is allocated externally.
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - the device where the stream
was originally allocated. If device is specified incorrectly,
subsequent launches using this stream may fail.

Return type:

[*Stream*](torch.cuda.streams.Stream.html#torch.cuda.streams.Stream)