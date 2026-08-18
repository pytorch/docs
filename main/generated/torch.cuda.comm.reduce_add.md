# torch.cuda.comm.reduce_add

torch.cuda.comm.reduce_add(*inputs*, *destination=None*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/nn/parallel/comm.py#L70)

Sum tensors from multiple GPUs.

All inputs should have matching shapes, dtype, and layout. The output tensor
will be of the same shape, dtype, and layout.

Parameters:

- **inputs** (*Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - an iterable of tensors to add.
- **destination** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - a device on which the output will be
placed (default: current device).

Returns:

A tensor containing an elementwise sum of all inputs, placed on the
`destination` device.