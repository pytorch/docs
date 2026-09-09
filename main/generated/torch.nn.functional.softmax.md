# torch.nn.functional.softmax

torch.nn.functional.softmax(*input*, *dim=None*, *_stacklevel=3*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/c712ec6ebb4ecd2838e2cafb0bbc7a3c5acfe668/torch/nn/functional.py#L2176)

Apply a softmax function.

Softmax is defined as:

Softmax(xi)=exp⁡(xi)∑jexp⁡(xj)\text{Softmax}(x_{i}) = \frac{\exp(x_i)}{\sum_j \exp(x_j)}Softmax(xi​)=∑j​exp(xj​)exp(xi​)​

It is applied to all slices along dim, and will re-scale them so that the elements
lie in the range [0, 1] and sum to 1.

See [`Softmax`](torch.nn.Softmax.html#torch.nn.Softmax) for more details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - input
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - A dimension along which softmax will be computed.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is casted to `dtype` before the operation
is performed. This is useful for preventing data type overflows. Default: None.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Note

This function doesn't work directly with NLLLoss,
which expects the Log to be computed between the Softmax and itself.
Use log_softmax instead (it's faster and has better numerical properties).