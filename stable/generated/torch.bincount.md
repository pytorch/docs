# torch.bincount

torch.bincount(*input*, *weights=None*, *minlength=0*) → [Tensor](../tensors.html#torch.Tensor)

Count the frequency of each value in an array of non-negative ints.

The number of bins (size 1) is one larger than the largest value in
`input` unless `input` is empty, in which case the result is a
tensor of size 0. If `minlength` is specified, the number of bins is at least
`minlength` and if `input` is empty, then the result is tensor of size
`minlength` filled with zeros. If `n` is the value at position `i`,
`out[n] += weights[i]` if `weights` is specified else
`out[n] += 1`.

Note

This operation may produce nondeterministic gradients when given tensors on a CUDA device. See [Reproducibility](../notes/randomness.html) for more information.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - 1-d int tensor
- **weights** ([*Tensor*](../tensors.html#torch.Tensor)) - optional, weight for each value in the input tensor.
Should be of same size as input tensor.
- **minlength** ([*int*](https://docs.python.org/3/library/functions.html#int)) - optional, minimum number of bins. Should be non-negative.

Returns:

a tensor of shape `Size([max(input) + 1])` if
`input` is non-empty, else `Size(0)`

Return type:

output ([Tensor](../tensors.html#torch.Tensor))

Example:

```
>>> input = torch.randint(0, 8, (5,), dtype=torch.int64)
>>> weights = torch.linspace(0, 1, steps=5)
>>> input, weights
(tensor([4, 3, 6, 3, 4]),
 tensor([ 0.0000, 0.2500, 0.5000, 0.7500, 1.0000])

>>> torch.bincount(input)
tensor([0, 0, 0, 2, 2, 0, 1])

>>> input.bincount(weights)
tensor([0.0000, 0.0000, 0.0000, 1.0000, 1.0000, 0.0000, 0.5000])
```