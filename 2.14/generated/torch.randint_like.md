# torch.randint_like

torch.randint_like(*input*, *low=0*, *high*, *\**, *generator=None*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a tensor with the same shape as Tensor `input` filled with
random integers generated uniformly between `low` (inclusive) and
`high` (exclusive).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the size of `input` will determine size of the output tensor.
- **low** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Lowest integer to be drawn from the distribution. Default: 0.
- **high** ([*int*](https://docs.python.org/3/library/functions.html#int)) - One above the highest integer to be drawn from the distribution.

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