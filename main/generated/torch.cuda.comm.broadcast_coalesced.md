# torch.cuda.comm.broadcast_coalesced

torch.cuda.comm.broadcast_coalesced(*tensors*, *devices*, *buffer_size=10485760*)[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/nn/parallel/comm.py#L50)

Broadcast a sequence of tensors to the specified GPUs.

Small tensors are first coalesced into a buffer to reduce the number of synchronizations.

Parameters:

- **tensors** (*sequence*) - tensors to broadcast. Must be on the same device,
either CPU or GPU.
- **devices** (*Iterable**[*[*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - an iterable of GPU
devices, among which to broadcast.
- **buffer_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - maximum size of the buffer used for coalescing

Returns:

A tuple containing copies of `tensor`, placed on `devices`.