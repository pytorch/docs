# Dropout2d

*class*torch.nn.modules.dropout.Dropout2d(*p=0.5*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/nn/modules/dropout.py#L124)

Randomly zero out entire channels.

A channel is a 2D feature map,
e.g., the jjj-th channel of the iii-th sample in the
batched input is a 2D tensor input[i,j]\text{input}[i, j]input[i,j].

Each channel will be zeroed out independently on every forward call with
probability `p` using samples from a Bernoulli distribution.

Usually the input comes from `nn.Conv2d` modules.

As described in the paper
[Efficient Object Localization Using Convolutional Networks](https://arxiv.org/abs/1411.4280) ,
if adjacent pixels within feature maps are strongly correlated
(as is normally the case in early convolution layers) then i.i.d. dropout
will not regularize the activations and will otherwise just result
in an effective learning rate decrease.

In this case, `nn.Dropout2d()` will help promote independence between
feature maps and should be used instead.

Parameters:

- **p** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - probability of an element to be zero-ed.
- **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set to `True`, will do this operation
in-place

Warning

Due to historical reasons, this class will perform 1D channel-wise dropout
for 3D inputs (as done by `nn.Dropout1d`). Thus, it currently does NOT
support inputs without a batch dimension of shape (C,H,W)(C, H, W)(C,H,W). This
behavior will change in a future release to interpret 3D inputs as no-batch-dim
inputs. To maintain the old behavior, switch to `nn.Dropout1d`.

Shape:

- Input: (N,C,H,W)(N, C, H, W)(N,C,H,W) or (N,C,L)(N, C, L)(N,C,L).
- Output: (N,C,H,W)(N, C, H, W)(N,C,H,W) or (N,C,L)(N, C, L)(N,C,L) (same shape as input).

Examples:

```
>>> m = nn.Dropout2d(p=0.2)
>>> input = torch.randn(20, 16, 32, 32)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/nn/modules/dropout.py#L172)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)