# SobolEngine

*class*torch.quasirandom.SobolEngine(*dimension*, *scramble=False*, *seed=None*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/quasirandom.py#L6)

The `torch.quasirandom.SobolEngine` is an engine for generating
(scrambled) Sobol sequences. Sobol sequences are an example of low
discrepancy quasi-random sequences.

This implementation of an engine for Sobol sequences is capable of
sampling sequences up to a maximum dimension of 21201. It uses direction
numbers from [https://web.maths.unsw.edu.au/~fkuo/sobol/](https://web.maths.unsw.edu.au/~fkuo/sobol/) obtained using the
search criterion D(6) up to the dimension 21201. This is the recommended
choice by the authors.

References

- Art B. Owen. Scrambling Sobol and Niederreiter-Xing points.
Journal of Complexity, 14(4):466-489, December 1998.
- I. M. Sobol. The distribution of points in a cube and the accurate
evaluation of integrals.
Zh. Vychisl. Mat. i Mat. Phys., 7:784-802, 1967.

Parameters:

- **dimension** (*Int*) - The dimensionality of the sequence to be drawn
- **scramble** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Setting this to `True` will produce
scrambled Sobol sequences. Scrambling is
capable of producing better Sobol
sequences. Default: `False`.
- **seed** (*Int**,**optional*) - This is the seed for the scrambling. The seed
of the random number generator is set to this,
if specified. Otherwise, it uses a random seed.
Default: `None`

Examples:

```
>>> soboleng = torch.quasirandom.SobolEngine(dimension=5)
>>> soboleng.draw(3)
tensor([[0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
 [0.5000, 0.5000, 0.5000, 0.5000, 0.5000],
 [0.7500, 0.2500, 0.2500, 0.2500, 0.7500]])
```

draw(*n=1*, *out=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/quasirandom.py#L77)

Function to draw a sequence of `n` points from a Sobol sequence.
Note that the samples are dependent on the previous samples. The size
of the result is (n,dimension)(n, dimension)(n,dimension).

Parameters:

- **n** (*Int**,**optional*) - The length of sequence of points to draw.
Default: 1
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - The output tensor
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of the
returned tensor.
Default: `None`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

draw_base2(*m*, *out=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/quasirandom.py#L130)

Function to draw a sequence of `2**m` points from a Sobol sequence.
Note that the samples are dependent on the previous samples. The size
of the result is (2∗∗m,dimension)(2**m, dimension)(2∗∗m,dimension).

Parameters:

- **m** (*Int*) - The (base2) exponent of the number of points to draw.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - The output tensor
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of the
returned tensor.
Default: `None`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

fast_forward(*n*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/quasirandom.py#L168)

Function to fast-forward the state of the `SobolEngine` by
`n` steps. This is equivalent to drawing `n` samples
without using the samples.

Parameters:

**n** (*Int*) - The number of steps to fast-forward by.

reset()[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/quasirandom.py#L160)

Function to reset the `SobolEngine` to base state.