# torch.nn.functional.conv1d

torch.nn.functional.conv1d(*input*, *weight*, *bias=None*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/55d182046edce7face6d9eb894f23b3a2588d876/torch/nn/functional.py#L53)

Applies a 1D convolution over an input signal composed of several input
planes.

This operator supports [TensorFloat32](../notes/cuda.html#tf32-on-ampere).

See [`Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d) for details and output shape.

Note

In some circumstances when given tensors on a CUDA device and using CuDNN, this operator may select a nondeterministic algorithm to increase performance. If this is undesirable, you can try to make the operation deterministic (potentially at a performance cost) by setting `torch.backends.cudnn.deterministic = True`. See [Reproducibility](../notes/randomness.html) for more information.

Note

This operator supports complex data types i.e. `complex32, complex64, complex128`.

Parameters:

- **input** - input tensor of shape (minibatch,in_channels,iW)(\text{minibatch} , \text{in\_channels} , iW)(minibatch,in_channels,iW)
- **weight** - filters of shape (out_channels,in_channelsgroups,kW)(\text{out\_channels} , \frac{\text{in\_channels}}{\text{groups}} , kW)(out_channels,groupsin_channels​,kW)
- **bias** - optional bias of shape (out_channels)(\text{out\_channels})(out_channels). Default: `None`
- **stride** - the stride of the convolving kernel. Can be a single number or
a one-element tuple (sW,). Default: 1
- **padding** -

implicit paddings on both sides of the input. Can be a string {'valid', 'same'},
single number or a one-element tuple (padW,). Default: 0
`padding='valid'` is the same as no padding. `padding='same'` pads
the input so the output has the same shape as the input. However, this mode
doesn't support any stride values other than 1.

Warning

For `padding='same'`, if the `weight` is even-length and
`dilation` is odd in any dimension, a full [`pad()`](torch.nn.functional.pad.html#torch.nn.functional.pad) operation
may be needed internally. Lowering performance.
- **dilation** - the spacing between kernel elements. Can be a single number or
a one-element tuple (dW,). Default: 1
- **groups** - split input into groups, in_channels\text{in\_channels}in_channels should be divisible by
the number of groups. Default: 1

Examples:

```
>>> inputs = torch.randn(33, 16, 30)
>>> filters = torch.randn(20, 16, 5)
>>> F.conv1d(inputs, filters)
```