# torch.distributions.utils.tril_matrix_to_vec

torch.distributions.utils.tril_matrix_to_vec(*mat*, *diag=0*)[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/distributions/utils.py#L187)

Convert a D x D matrix or a batch of matrices into a (batched) vector
which comprises of lower triangular elements from the matrix in row order.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)