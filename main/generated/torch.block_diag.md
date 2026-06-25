# torch.block_diag

torch.block_diag(**tensors*)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/functional.py#L1447)

Create a block diagonal matrix from provided tensors.

Parameters:

***tensors** - One or more tensors with 0, 1, or 2 dimensions.

Returns:

A 2 dimensional tensor with all the input tensors arranged in
order such that their upper left and lower right corners are
diagonally adjacent. All other elements are set to 0.

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> import torch
>>> A = torch.tensor([[0, 1], [1, 0]])
>>> B = torch.tensor([[3, 4, 5], [6, 7, 8]])
>>> C = torch.tensor(7)
>>> D = torch.tensor([1, 2, 3])
>>> E = torch.tensor([[4], [5], [6]])
>>> torch.block_diag(A, B, C, D, E)
tensor([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 3, 4, 5, 0, 0, 0, 0, 0],
 [0, 0, 6, 7, 8, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 7, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 2, 3, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 6]])
```