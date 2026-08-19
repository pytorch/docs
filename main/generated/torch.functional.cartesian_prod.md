# torch.functional.cartesian_prod

torch.functional.cartesian_prod(**tensors*)[[source]](https://github.com/pytorch/pytorch/blob/3af07571b9d7402fd74352d079e6ff5fa307ec5f/torch/functional.py#L1412)

Do cartesian product of the given sequence of tensors. The behavior is similar to
python's itertools.product.

Parameters:

***tensors** ([*Tensor*](../tensors.html#torch.Tensor)) - any number of 1 dimensional tensors.

Returns:

A tensor equivalent to converting all the input tensors into lists,
do itertools.product on these lists, and finally convert the resulting list
into tensor.

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> import itertools
>>> a = [1, 2, 3]
>>> b = [4, 5]
>>> list(itertools.product(a, b))
[(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
>>> tensor_a = torch.tensor(a)
>>> tensor_b = torch.tensor(b)
>>> torch.cartesian_prod(tensor_a, tensor_b)
tensor([[1, 4],
 [1, 5],
 [2, 4],
 [2, 5],
 [3, 4],
 [3, 5]])
```