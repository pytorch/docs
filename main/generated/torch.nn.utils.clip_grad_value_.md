# torch.nn.utils.clip_grad_value_

torch.nn.utils.clip_grad_value_(*parameters*, *clip_value*, *foreach=None*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/nn/utils/clip_grad.py#L256)

Clip the gradients of an iterable of parameters at specified value.

Gradients are modified in-place.

Parameters:

- **parameters** (*Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*] or*[*Tensor*](../tensors.html#torch.Tensor)) - an iterable of Tensors or a
single Tensor that will have gradients normalized
- **clip_value** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) - maximum allowed value of the gradients.
The gradients are clipped in the range
[-clip_value,clip_value]\left[\text{-clip\_value}, \text{clip\_value}\right][-clip_value,clip_value]
- **foreach** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - use the faster foreach-based implementation
If `None`, use the foreach implementation for CUDA and CPU native tensors and
silently fall back to the slow implementation for other device types.
Default: `None`