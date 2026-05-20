# torch.cuda.comm.reduce_add_coalesced

torch.cuda.comm.reduce_add_coalesced(*inputs*, *destination=None*, *buffer_size=10485760*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/nn/parallel/comm.py#L124)

Sum tensors from multiple GPUs.

Small tensors are first coalesced into a buffer to reduce the number
of synchronizations.

Parameters:

- **inputs** (*Iterable**[**Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*]**]*) - iterable of iterables that
contain tensors from a single device.
- **destination** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - a device on which the output will be
placed (default: current device).
- **buffer_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - maximum size of the buffer used for coalescing

Returns:

A tuple of tensors containing an elementwise sum of each group of
inputs, placed on the `destination` device.