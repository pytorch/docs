# Dropout1d

*class*torch.nn.Dropout1d(*p=0.5*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/nn/modules/dropout.py#L76)

Randomly zero out entire channels.

A channel is a 1D feature map,
e.g., the jjj-th channel of the iii-th sample in the
batched input is a 1D tensor input[i,j]\text{input}[i, j]input[i,j].

Each channel will be zeroed out independently on every forward call with
probability `p` using samples from a Bernoulli distribution.

Usually the input comes from `nn.Conv1d` modules.

As described in the paper
[Efficient Object Localization Using Convolutional Networks](https://arxiv.org/abs/1411.4280) ,
if adjacent pixels within feature maps are strongly correlated
(as is normally the case in early convolution layers) then i.i.d. dropout
will not regularize the activations and will otherwise just result
in an effective learning rate decrease.

In this case, `nn.Dropout1d()` will help promote independence between
feature maps and should be used instead.

Parameters:

- **p** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - probability of an element to be zero-ed.
- **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set to `True`, will do this operation
in-place

Shape:

- Input: (N,C,L)(N, C, L)(N,C,L) or (C,L)(C, L)(C,L).
- Output: (N,C,L)(N, C, L)(N,C,L) or (C,L)(C, L)(C,L) (same shape as input).

Examples:

```
>>> m = nn.Dropout1d(p=0.2)
>>> input = torch.randn(20, 16, 32)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/nn/modules/dropout.py#L117)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)