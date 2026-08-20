# torch.cuda.comm.broadcast

torch.cuda.comm.broadcast(*tensor*, *devices=None*, ***, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/nn/parallel/comm.py#L16)

Broadcasts a tensor to specified GPU devices.

Parameters:

- **tensor** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor to broadcast. Can be on CPU or GPU.
- **devices** (*Iterable**[*[*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - an iterable of
GPU devices, among which to broadcast.
- **out** (*Sequence**[*[*Tensor*](../tensors.html#torch.Tensor)*]**,**optional**,**keyword-only*) - the GPU tensors to
store output results.

Note

Exactly one of `devices` and `out` must be specified.

Returns:

- If `devices` is specified,

a tuple containing copies of `tensor`, placed on
`devices`.
- If `out` is specified,

a tuple containing `out` tensors, each containing a copy of
`tensor`.