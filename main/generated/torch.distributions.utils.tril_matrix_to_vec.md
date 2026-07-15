# torch.distributions.utils.tril_matrix_to_vec

torch.distributions.utils.tril_matrix_to_vec(*mat*, *diag=0*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/distributions/utils.py#L187)

Convert a D x D matrix or a batch of matrices into a (batched) vector
which comprises of lower triangular elements from the matrix in row order.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)