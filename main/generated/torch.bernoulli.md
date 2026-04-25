# torch.bernoulli

torch.bernoulli(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *generator: [Generator](torch.Generator.html#torch.Generator) | [None](https://docs.python.org/3/library/constants.html#None)*, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Draws binary random numbers (0 or 1) from a Bernoulli distribution.

The `input` tensor should be a tensor containing probabilities
to be used for drawing the binary random number.
Hence, all values in `input` have to be in the range:
0≤inputi≤10 \leq \text{input}_i \leq 10≤inputi​≤1.

The ith\text{i}^{th}ith element of the output tensor will draw a
value 111 according to the ith\text{i}^{th}ith probability value given
in `input`.

outi∼Bernoulli(p=inputi)\text{out}_{i} \sim \mathrm{Bernoulli}(p = \text{input}_{i})

outi​∼Bernoulli(p=inputi​)

The returned `out` tensor only has values 0 or 1 and is of the same
shape as `input`.

`out` can have integral `dtype`, but `input` must have floating
point `dtype`.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor of probability values for the Bernoulli distribution

Keyword Arguments:

- **generator** ([`torch.Generator`](torch.Generator.html#torch.Generator), optional) - a pseudorandom number generator for sampling
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.empty(3, 3).uniform_(0, 1) # generate a uniform random matrix with range [0, 1]
>>> a
tensor([[ 0.1737, 0.0950, 0.3609],
 [ 0.7148, 0.0289, 0.2676],
 [ 0.9456, 0.8937, 0.7202]])
>>> torch.bernoulli(a)
tensor([[ 1., 0., 0.],
 [ 0., 0., 0.],
 [ 1., 1., 1.]])

>>> a = torch.ones(3, 3) # probability of drawing "1" is 1
>>> torch.bernoulli(a)
tensor([[ 1., 1., 1.],
 [ 1., 1., 1.],
 [ 1., 1., 1.]])
>>> a = torch.zeros(3, 3) # probability of drawing "1" is 0
>>> torch.bernoulli(a)
tensor([[ 0., 0., 0.],
 [ 0., 0., 0.],
 [ 0., 0., 0.]])
```