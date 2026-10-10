# torch.distributions.utils.tril_matrix_to_vec

torch.distributions.utils.tril_matrix_to_vec(*mat*, *diag=0*)[[source]](https://github.com/pytorch/pytorch/blob/1b51ed6169475ed863f4ee43b7eaa52ecda0f862/torch/distributions/utils.py#L187)

Convert a D x D matrix or a batch of matrices into a (batched) vector
which comprises lower triangular elements from the matrix in row order.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)