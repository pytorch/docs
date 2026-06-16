# Buffer

*class*torch.nn.parameter.Buffer(*data=None*, ***, *persistent=True*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/nn/parameter.py#L249)

A kind of Tensor that should not be considered a model
parameter. For example, BatchNorm's `running_mean` is not a parameter, but is part of the module's state.

Buffers are [`Tensor`](../tensors.html#torch.Tensor) subclasses, that have a
very special property when used with `Module` s - when they're
assigned as Module attributes they are automatically added to the list of
its buffers, and will appear e.g. in [`buffers()`](torch.nn.Module.html#torch.nn.Module.buffers) iterator.
Assigning a Tensor doesn't have such effect. One can still assign a Tensor as explicitly by using
the [`register_buffer()`](torch.nn.Module.html#torch.nn.Module.register_buffer) function.

Parameters:

- **data** ([*Tensor*](../tensors.html#torch.Tensor)) - buffer tensor.
- **persistent** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the buffer is part of the module's
`state_dict`. Default: `True`