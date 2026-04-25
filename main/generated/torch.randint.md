# torch.randint

torch.randint(*low=0*, *high*, *size*, *\**, *generator=None*, *out=None*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a tensor filled with random integers generated uniformly
between `low` (inclusive) and `high` (exclusive).

The shape of the tensor is defined by the variable argument `size`.

Note

With the global dtype default (`torch.float32`), this function returns
a tensor with dtype `torch.int64`.

Parameters:

- **low** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Lowest integer to be drawn from the distribution. Default: 0.
- **high** ([*int*](https://docs.python.org/3/library/functions.html#int)) - One above the highest integer to be drawn from the distribution.
- **size** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - a tuple defining the shape of the output tensor.

Keyword Arguments:

- **generator** ([`torch.Generator`](torch.Generator.html#torch.Generator), optional) - a pseudorandom number generator for sampling
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.
- **dtype** ([*torch.dtype*](../tensor_attributes.html#torch.dtype)*,**optional*) - the desired data type of returned tensor. Default: if `None`,
this function returns a tensor with dtype `torch.int64`.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). [`device`](../tensor_attributes.html#torch.device) will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.

Example:

```
>>> torch.randint(3, 5, (3,))
tensor([4, 3, 4])

>>> torch.randint(10, (2, 2))
tensor([[0, 2],
 [5, 5]])

>>> torch.randint(3, 10, (2, 2))
tensor([[4, 5],
 [6, 7]])
```