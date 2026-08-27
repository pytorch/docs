# torch.cuda.comm.reduce_add_coalesced

torch.cuda.comm.reduce_add_coalesced(*inputs*, *destination=None*, *buffer_size=10485760*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/nn/parallel/comm.py#L124)

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