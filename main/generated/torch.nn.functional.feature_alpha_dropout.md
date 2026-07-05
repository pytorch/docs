# torch.nn.functional.feature_alpha_dropout

torch.nn.functional.feature_alpha_dropout(*input*, *p=0.5*, *training=False*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/nn/functional.py#L1687)

Randomly masks out entire channels (a channel is a feature map).

For example, the jjj-th channel of the iii-th sample in the batch input
is a tensor input[i,j]\text{input}[i, j]input[i,j] of the input tensor. Instead of
setting activations to zero, as in regular Dropout, the activations are set
to the negative saturation value of the SELU activation function.

Each element will be masked independently on every forward call with
probability `p` using samples from a Bernoulli distribution.
The elements to be masked are randomized on every forward call, and scaled
and shifted to maintain zero mean and unit variance.

See [`FeatureAlphaDropout`](torch.nn.FeatureAlphaDropout.html#torch.nn.FeatureAlphaDropout) for details.

Parameters:

- **p** ([*float*](https://docs.python.org/3/library/functions.html#float)) - dropout probability of a channel to be zeroed. Default: 0.5
- **training** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - apply dropout if is `True`. Default: `True`
- **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to `True`, will do this operation in-place. Default: `False`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)