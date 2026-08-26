# torch.nn.functional.conv_transpose3d

torch.nn.functional.conv_transpose3d(*input*, *weight*, *bias=None*, *stride=1*, *padding=0*, *output_padding=0*, *groups=1*, *dilation=1*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/nn/functional.py#L287)

Applies a 3D transposed convolution operator over an input image
composed of several input planes, sometimes also called "deconvolution"

This operator supports [TensorFloat32](../notes/cuda.html#tf32-on-ampere).

See [`ConvTranspose3d`](torch.nn.ConvTranspose3d.html#torch.nn.ConvTranspose3d) for details and output shape.

Note

In some circumstances when given tensors on a CUDA device and using CuDNN, this operator may select a nondeterministic algorithm to increase performance. If this is undesirable, you can try to make the operation deterministic (potentially at a performance cost) by setting `torch.backends.cudnn.deterministic = True`. See [Reproducibility](../notes/randomness.html) for more information.

Parameters:

- **input** - input tensor of shape (minibatch,in_channels,iT,iH,iW)(\text{minibatch} , \text{in\_channels} , iT , iH , iW)(minibatch,in_channels,iT,iH,iW)
- **weight** - filters of shape (in_channels,out_channelsgroups,kT,kH,kW)(\text{in\_channels} , \frac{\text{out\_channels}}{\text{groups}} , kT , kH , kW)(in_channels,groupsout_channels​,kT,kH,kW)
- **bias** - optional bias of shape (out_channels)(\text{out\_channels})(out_channels). Default: None
- **stride** - the stride of the convolving kernel. Can be a single number or a
tuple `(sT, sH, sW)`. Default: 1
- **padding** - `dilation * (kernel_size - 1) - padding` zero-padding will be added to both
sides of each dimension in the input. Can be a single number or a tuple
`(padT, padH, padW)`. Default: 0
- **output_padding** - additional size added to one side of each dimension in the
output shape. Can be a single number or a tuple
`(out_padT, out_padH, out_padW)`. Default: 0
- **groups** - split input into groups, in_channels\text{in\_channels}in_channels should be divisible by the
number of groups. Default: 1
- **dilation** - the spacing between kernel elements. Can be a single number or
a tuple (dT, dH, dW). Default: 1

Examples:

```
>>> inputs = torch.randn(20, 16, 50, 10, 20)
>>> weights = torch.randn(16, 33, 3, 3, 3)
>>> F.conv_transpose3d(inputs, weights)
```