# torch.nn.functional.dropout

torch.nn.functional.dropout(*input*, *p=0.5*, *training=True*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/nn/functional.py#L1425)

During training, randomly zeroes some elements of the input tensor with probability `p`.

Uses samples from a Bernoulli distribution.

See [`Dropout`](torch.nn.Dropout.html#torch.nn.Dropout) for details.

Parameters:

- **p** ([*float*](https://docs.python.org/3/library/functions.html#float)) - probability of an element to be zeroed. Default: 0.5
- **training** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - apply dropout if is `True`. Default: `True`
- **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to `True`, will do this operation in-place. Default: `False`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)