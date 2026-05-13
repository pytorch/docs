# torch.multinomial

torch.multinomial(*input*, *num_samples*, *replacement=False*, ***, *generator=None*, *out=None*) → LongTensor

Returns a tensor where each row contains `num_samples` indices sampled
from the multinomial (a stricter definition would be multivariate,
refer to [`torch.distributions.multinomial.Multinomial`](../distributions.html#torch.distributions.multinomial.Multinomial) for more details)
probability distribution located in the corresponding row
of tensor `input`.

Note

The rows of `input` do not need to sum to one (in which case we use
the values as weights), but must be non-negative, finite and have
a non-zero sum.

Indices are ordered from left to right according to when each was sampled
(first samples are placed in first column).

If `input` is a vector, `out` is a vector of size `num_samples`.

If `input` is a matrix with m rows, `out` is an matrix of shape
(m×num_samples)(m \times \text{num\_samples})(m×num_samples).

If replacement is `True`, samples are drawn with replacement.

If not, they are drawn without replacement, which means that when a
sample index is drawn for a row, it cannot be drawn again for that row.

Note

When drawn without replacement, `num_samples` must be lower than
number of non-zero elements in `input` (or the min number of non-zero
elements in each row of `input` if it is a matrix).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor containing probabilities
- **num_samples** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of samples to draw
- **replacement** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to draw with replacement or not

Keyword Arguments:

- **generator** ([`torch.Generator`](torch.Generator.html#torch.Generator), optional) - a pseudorandom number generator for sampling
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> weights = torch.tensor([0, 10, 3, 0], dtype=torch.float) # create a tensor of weights
>>> torch.multinomial(weights, 2)
tensor([1, 2])
>>> torch.multinomial(weights, 5) # ERROR!
RuntimeError: cannot sample n_sample > prob_dist.size(-1) samples without replacement
>>> torch.multinomial(weights, 4, replacement=True)
tensor([ 2, 1, 1, 1])
```