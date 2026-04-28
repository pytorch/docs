# torch.clone

torch.clone(*input*, ***, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a copy of `input`.

Note

This function is differentiable, so gradients will flow back from the
result of this operation to `input`. To create a tensor without an
autograd relationship to `input` see [`detach()`](torch.Tensor.detach.html#torch.Tensor.detach).

In addition, when `torch.preserve_format` is used:
If the input tensor is dense (i.e., non-overlapping strided),
its memory format (including strides) is retained.
Otherwise (e.g., a non-dense view like a stepped slice),
the output is converted to the dense (contiguous) format.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned tensor. Default: `torch.preserve_format`.