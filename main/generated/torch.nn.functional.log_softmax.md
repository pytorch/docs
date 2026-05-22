# torch.nn.functional.log_softmax

torch.nn.functional.log_softmax(*input*, *dim=None*, *_stacklevel=3*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/54541f51bee1b9b66a0ecb11e69067a677a60487/torch/nn/functional.py#L2245)

Apply a softmax followed by a logarithm.

While mathematically equivalent to log(softmax(x)), doing these two
operations separately is slower and numerically unstable. This function
uses an alternative formulation to compute the output and gradient correctly.

See [`LogSoftmax`](torch.nn.LogSoftmax.html#torch.nn.LogSoftmax) for more details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - input
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - A dimension along which log_softmax will be computed.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is cast to `dtype` before the operation
is performed. This is useful for preventing data type overflows. Default: None.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)