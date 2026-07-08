# Dropout

*class*torch.nn.Dropout(*p=0.5*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/502e93eb52e0fcf07a908796ccd61af06c4b58b9/torch/nn/modules/dropout.py#L35)

During training, randomly zeroes some of the elements of the input tensor with probability `p`.

The zeroed elements are chosen independently for each forward call and are sampled from a Bernoulli distribution.

Each channel will be zeroed out independently on every forward call.

This has proven to be an effective technique for regularization and
preventing the co-adaptation of neurons as described in the paper
[Improving neural networks by preventing co-adaptation of feature
detectors](https://arxiv.org/abs/1207.0580) .

Furthermore, the outputs are scaled by a factor of 11−p\frac{1}{1-p}1−p1​ during
training. This means that during evaluation the module simply computes an
identity function.

Parameters:

- **p** ([*float*](https://docs.python.org/3/library/functions.html#float)) - probability of an element to be zeroed. Default: 0.5
- **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to `True`, will do this operation in-place. Default: `False`

Shape:

- Input: (∗)(*)(∗). Input can be of any shape
- Output: (∗)(*)(∗). Output is of the same shape as input

Examples:

```
>>> m = nn.Dropout(p=0.2)
>>> input = torch.randn(20, 16)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/502e93eb52e0fcf07a908796ccd61af06c4b58b9/torch/nn/modules/dropout.py#L69)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)