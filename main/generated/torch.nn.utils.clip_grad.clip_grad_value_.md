# torch.nn.utils.clip_grad.clip_grad_value_

torch.nn.utils.clip_grad.clip_grad_value_(*parameters*, *clip_value*, *foreach=None*)[[source]](https://github.com/pytorch/pytorch/blob/f7811aa3c052ace6751fbc2f6bc93908b9ea6b9f/torch/nn/utils/clip_grad.py#L256)

Clip the gradients of an iterable of parameters at specified value.

Gradients are modified in-place.

Parameters:

- **parameters** (*Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*] or*[*Tensor*](../tensors.html#torch.Tensor)) - an iterable of Tensors or a
single Tensor that will have gradients normalized
- **clip_value** ([*float*](https://docs.python.org/3/library/functions.html#float)) - maximum allowed value of the gradients.
The gradients are clipped in the range
[-clip_value,clip_value]\left[\text{-clip\_value}, \text{clip\_value}\right][-clip_value,clip_value]
- **foreach** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - use the faster foreach-based implementation
If `None`, use the foreach implementation for CUDA and CPU native tensors and
silently fall back to the slow implementation for other device types.
Default: `None`