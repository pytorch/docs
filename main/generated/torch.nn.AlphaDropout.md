# AlphaDropout

*class*torch.nn.AlphaDropout(*p=0.5*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/nn/modules/dropout.py#L227)

Applies Alpha Dropout over the input.

Alpha Dropout is a type of Dropout that maintains the self-normalizing
property.
For an input with zero mean and unit standard deviation, the output of
Alpha Dropout maintains the original mean and standard deviation of the
input.
Alpha Dropout goes hand-in-hand with SELU activation function, which ensures
that the outputs have zero mean and unit standard deviation.

During training, it randomly masks some of the elements of the input
tensor with probability *p* using samples from a bernoulli distribution.
The elements to be masked are randomized on every forward call, and scaled
and shifted to maintain zero mean and unit standard deviation.

During evaluation the module simply computes an identity function.

More details can be found in the paper [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515) .

Parameters:

- **p** ([*float*](https://docs.python.org/3/library/functions.html#float)) - probability of an element to be dropped. Default: 0.5
- **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set to `True`, will do this operation
in-place

Shape:

- Input: (∗)(*)(∗). Input can be of any shape
- Output: (∗)(*)(∗). Output is of the same shape as input

Examples:

```
>>> m = nn.AlphaDropout(p=0.2)
>>> input = torch.randn(20, 16)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/nn/modules/dropout.py#L265)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)