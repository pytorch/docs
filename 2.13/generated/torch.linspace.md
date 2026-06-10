# torch.linspace

torch.linspace(*start*, *end*, *steps*, ***, *out=None*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*) → [Tensor](../tensors.html#torch.Tensor)

Creates a one-dimensional tensor of size `steps` whose values are evenly
spaced from `start` to `end`, inclusive. That is, the value are:

(start,start+end−startsteps−1,...,start+(steps−2)∗end−startsteps−1,end)(\text{start},
\text{start} + \frac{\text{end} - \text{start}}{\text{steps} - 1},
\ldots,
\text{start} + (\text{steps} - 2) * \frac{\text{end} - \text{start}}{\text{steps} - 1},
\text{end})

(start,start+steps−1end−start​,...,start+(steps−2)∗steps−1end−start​,end)

From PyTorch 1.11 linspace requires the steps argument. Use steps=100 to restore the previous behavior.

Parameters:

- **start** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](../tensors.html#torch.Tensor)) - the starting value for the set of points. If Tensor, it must be 0-dimensional
- **end** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](../tensors.html#torch.Tensor)) - the ending value for the set of points. If Tensor, it must be 0-dimensional
- **steps** ([*int*](https://docs.python.org/3/library/functions.html#int)) - size of the constructed tensor

Keyword Arguments:

- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.
- **dtype** ([*torch.dtype*](../tensor_attributes.html#torch.dtype)*,**optional*) - the data type to perform the computation in.
Default: if None, uses the global default dtype (see torch.get_default_dtype())
when both `start` and `end` are real,
and corresponding complex dtype when either is complex.
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
>>> torch.linspace(3, 10, steps=5)
tensor([ 3.0000, 4.7500, 6.5000, 8.2500, 10.0000])
>>> torch.linspace(-10, 10, steps=5)
tensor([-10., -5., 0., 5., 10.])
>>> torch.linspace(start=-10, end=10, steps=5)
tensor([-10., -5., 0., 5., 10.])
>>> torch.linspace(start=-10, end=10, steps=1)
tensor([-10.])
```