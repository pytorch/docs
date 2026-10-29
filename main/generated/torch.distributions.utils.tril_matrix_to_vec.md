# torch.distributions.utils.tril_matrix_to_vec

torch.distributions.utils.tril_matrix_to_vec(*mat*, *diag=0*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/distributions/utils.py#L187)

Convert a D x D matrix or a batch of matrices into a (batched) vector
which comprises lower triangular elements from the matrix in row order.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)