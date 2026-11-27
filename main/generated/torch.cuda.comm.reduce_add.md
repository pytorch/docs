# torch.cuda.comm.reduce_add

torch.cuda.comm.reduce_add(*inputs*, *destination=None*)[[source]](https://github.com/pytorch/pytorch/blob/5f228673c58f6d36691c0cbc5c677fdf0c349372/torch/nn/parallel/comm.py#L70)

Sum tensors from multiple GPUs.

All inputs should have matching shapes, dtype, and layout. The output tensor
will be of the same shape, dtype, and layout.

Parameters:

- **inputs** (*Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - an iterable of tensors to add.
- **destination** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - a device on which the output will be
placed (default: current device).

Returns:

A tensor containing an elementwise sum of all inputs, placed on the
`destination` device.