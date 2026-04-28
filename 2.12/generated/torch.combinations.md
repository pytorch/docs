# torch.combinations

torch.combinations(*input: [Tensor](../tensors.html#torch.Tensor)*, *r: [int](https://docs.python.org/3/library/functions.html#int) = 2*, *with_replacement: [bool](https://docs.python.org/3/library/functions.html#bool) = False*) → seq

Compute combinations of length rrr of the given tensor. The behavior is similar to
python's itertools.combinations when with_replacement is set to False, and
itertools.combinations_with_replacement when with_replacement is set to True.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - 1D vector.
- **r** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - number of elements to combine
- **with_replacement** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to allow duplication in combination

Returns:

A tensor equivalent to converting all the input tensors into lists, do
itertools.combinations or itertools.combinations_with_replacement on these
lists, and finally convert the resulting list into tensor.

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> a = [1, 2, 3]
>>> list(itertools.combinations(a, r=2))
[(1, 2), (1, 3), (2, 3)]
>>> list(itertools.combinations(a, r=3))
[(1, 2, 3)]
>>> list(itertools.combinations_with_replacement(a, r=2))
[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
>>> tensor_a = torch.tensor(a)
>>> torch.combinations(tensor_a)
tensor([[1, 2],
 [1, 3],
 [2, 3]])
>>> torch.combinations(tensor_a, r=3)
tensor([[1, 2, 3]])
>>> torch.combinations(tensor_a, with_replacement=True)
tensor([[1, 1],
 [1, 2],
 [1, 3],
 [2, 2],
 [2, 3],
 [3, 3]])
```