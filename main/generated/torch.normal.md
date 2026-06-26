# torch.normal

torch.normal(*mean*, *std*, ***, *generator=None*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a tensor of random numbers drawn from separate normal distributions
whose mean and standard deviation are given.

The [`mean`](torch.mean.html#torch.mean) is a tensor with the mean of
each output element's normal distribution

The [`std`](torch.std.html#torch.std) is a tensor with the standard deviation of
each output element's normal distribution

The shapes of [`mean`](torch.mean.html#torch.mean) and [`std`](torch.std.html#torch.std) don't need to match, but the
total number of elements in each tensor need to be the same.

Note

When the shapes do not match, the shape of [`mean`](torch.mean.html#torch.mean)
is used as the shape for the returned output tensor

Note

When [`std`](torch.std.html#torch.std) is a CUDA tensor, this function synchronizes
its device with the CPU.

Parameters:

- **mean** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](../tensors.html#torch.Tensor)) - per-element mean(s). Only floating point types are supported.
- **std** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](../tensors.html#torch.Tensor)) - per-element standard deviation(s). Only floating point types are supported.

Keyword Arguments:

- **generator** ([`torch.Generator`](torch.Generator.html#torch.Generator), optional) - a pseudorandom number generator for sampling
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.normal(mean=torch.arange(1., 11.), std=torch.arange(1, 0, -0.1))
tensor([ 1.0425, 3.5672, 2.7969, 4.2925, 4.7229, 6.2134,
 8.0505, 8.1408, 9.0563, 10.0566])
```

torch.normal(*mean=0.0*, *std*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Similar to the function above, but the means are shared among all drawn
elements.

Parameters:

- **mean** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - the mean for all distributions
- **std** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor of per-element standard deviations

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.normal(mean=0.5, std=torch.arange(1., 6.))
tensor([-1.2793, -1.0732, -2.0687, 5.1177, -1.2303])
```

torch.normal(*mean*, *std=1.0*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Similar to the function above, but the standard deviations are shared among
all drawn elements.

Parameters:

- **mean** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor of per-element means
- **std** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - the standard deviation for all distributions

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor

Example:

```
>>> torch.normal(mean=torch.arange(1., 6.))
tensor([ 1.1552, 2.6148, 2.6535, 5.8318, 4.2361])
```

torch.normal(*mean*, *std*, *size*, ***, *generator=None*, *out=None*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Similar to the function above, but the means and standard deviations are shared
among all drawn elements. The resulting tensor has size given by `size`.

Parameters:

- **mean** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the mean for all distributions
- **std** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the standard deviation for all distributions
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)*...*) - a sequence of integers defining the shape of the output tensor.

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
>>> torch.normal(2, 3, size=(1, 4))
tensor([[-1.3987, -1.9544, 3.6048, 0.7909]])
```