# torch.randn_like

torch.randn_like(*input*, ***, *generator=None*, *dtype=None*, *layout=None*, *device=None*, *requires_grad=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a tensor with the same size as `input` that is filled with
random numbers from a normal distribution with mean 0 and variance 1. Please refer to [`torch.randn()`](torch.randn.html#torch.randn) for the
sampling process of complex dtypes. `torch.randn_like(input)` is equivalent to
`torch.randn(input.size(), dtype=input.dtype, layout=input.layout, device=input.device)`.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the size of `input` will determine size of the output tensor.

Keyword Arguments:

- **generator** ([`torch.Generator`](torch.Generator.html#torch.Generator), optional) - a pseudorandom number generator for sampling.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned Tensor.
Default: if `None`, defaults to the dtype of `input`.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned tensor.
Default: if `None`, defaults to the layout of `input`.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, defaults to the device of `input`.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.
- **memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.