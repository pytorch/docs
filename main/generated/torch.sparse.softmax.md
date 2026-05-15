# torch.sparse.softmax

torch.sparse.softmax(*input*, *dim*, ***, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/sparse/__init__.py#L286)

Applies a softmax function.

Softmax is defined as:

Softmax(xi)=exp(xi)∑jexp(xj)\text{Softmax}(x_{i}) = \frac{exp(x_i)}{\sum_j exp(x_j)}Softmax(xi​)=∑j​exp(xj​)exp(xi​)​

where i,ji, ji,j run over sparse tensor indices and unspecified
entries are ignores. This is equivalent to defining unspecified
entries as negative infinity so that exp(xk)=0exp(x_k) = 0exp(xk​)=0 when the
entry with index kkk has not specified.

It is applied to all slices along dim, and will re-scale them so
that the elements lie in the range [0, 1] and sum to 1.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - input
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - A dimension along which softmax will be computed.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type
of returned tensor. If specified, the input tensor is
casted to `dtype` before the operation is
performed. This is useful for preventing data type
overflows. Default: None