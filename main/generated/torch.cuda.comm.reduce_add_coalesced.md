# torch.cuda.comm.reduce_add_coalesced

torch.cuda.comm.reduce_add_coalesced(*inputs*, *destination=None*, *buffer_size=10485760*)[[source]](https://github.com/pytorch/pytorch/blob/52b7da3f54bb5af4e72fc6040fc43f091267ad09/torch/nn/parallel/comm.py#L124)

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