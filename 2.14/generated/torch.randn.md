# torch.randn

torch.randn(**size*, ***, *generator=None*, *out=None*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a tensor filled with random numbers from a normal distribution
with mean 0 and variance 1 (also called the standard normal
distribution).

outi∼N(0,1)\text{out}_{i} \sim \mathcal{N}(0, 1)

outi​∼N(0,1)

For complex dtypes, the tensor is i.i.d. sampled from a [complex normal distribution](https://en.wikipedia.org/wiki/Complex_normal_distribution) with zero mean and
unit variance as

outi∼CN(0,1)\text{out}_{i} \sim \mathcal{CN}(0, 1)

outi​∼CN(0,1)

This is equivalent to separately sampling the real (Re⁡)(\operatorname{Re})(Re) and imaginary
(Im⁡)(\operatorname{Im})(Im) part of outi\text{out}_iouti​ as

Re⁡(outi)∼N(0,12),Im⁡(outi)∼N(0,12)\operatorname{Re}(\text{out}_{i}) \sim \mathcal{N}(0, \frac{1}{2}),\quad
\operatorname{Im}(\text{out}_{i}) \sim \mathcal{N}(0, \frac{1}{2})

Re(outi​)∼N(0,21​),Im(outi​)∼N(0,21​)

The shape of the tensor is defined by the variable argument `size`.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)*...*) - a sequence of integers defining the shape of the output tensor.
Can be a variable number of arguments or a collection like a list or tuple.

Keyword Arguments:

- **generator** ([`torch.Generator`](torch.Generator.html#torch.Generator), optional) - a pseudorandom number generator for sampling
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](torch.set_default_dtype.html#torch.set_default_dtype)).
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). [`device`](../tensor_attributes.html#torch.device) will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.

Example:

```
>>> torch.randn(4)
tensor([-2.1436, 0.9966, 2.3426, -0.6366])
>>> torch.randn(2, 3)
tensor([[ 1.5954, 2.8929, -1.0923],
 [ 1.1719, -0.4709, -0.1996]])
```