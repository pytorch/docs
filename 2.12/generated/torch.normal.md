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

- **mean** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor of per-element means
- **std** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor of per-element standard deviations

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

torch.normal(*mean*, *std*, *size*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Similar to the function above, but the means and standard deviations are shared
among all drawn elements. The resulting tensor has size given by `size`.

Parameters:

- **mean** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the mean for all distributions
- **std** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the standard deviation for all distributions
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)*...*) - a sequence of integers defining the shape of the output tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.normal(2, 3, size=(1, 4))
tensor([[-1.3987, -1.9544, 3.6048, 0.7909]])
```