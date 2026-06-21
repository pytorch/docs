# ConvTranspose1d

*class*torch.nn.modules.conv.ConvTranspose1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *output_padding=0*, *groups=1*, *bias=True*, *dilation=1*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/modules/conv.py#L832)

Applies a 1D transposed convolution operator over an input image
composed of several input planes.

This module can be seen as the gradient of Conv1d with respect to its input.
It is also known as a fractionally-strided convolution or
a deconvolution (although it is not an actual deconvolution operation as it does
not compute a true inverse of convolution). For more information, see the visualizations
[here](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md) and the [Deconvolutional Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf) paper.

This module supports [TensorFloat32](../notes/cuda.html#tf32-on-ampere).

On certain ROCm devices, when using float16 inputs this module will use [different precision](../notes/numerical_accuracy.html#fp16-on-mi200) for backward.

- `stride` controls the stride for the cross-correlation.
- `padding` controls the amount of implicit zero padding on both
sides for `dilation * (kernel_size - 1) - padding` number of points. See note
below for details.
- `output_padding` controls the additional size added to one side
of the output shape. See note below for details.
- `dilation` controls the spacing between the kernel points; also known as the à trous algorithm.
It is harder to describe, but the link [here](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md) has a nice visualization of what `dilation` does.
- `groups` controls the connections between inputs and outputs.
`in_channels` and `out_channels` must both be divisible by
`groups`. For example,

> - At groups=1, all inputs are convolved to all outputs.
> - At groups=2, the operation becomes equivalent to having two conv
> layers side by side, each seeing half the input channels
> and producing half the output channels, and both subsequently
> concatenated.
> - At groups= `in_channels`, each input channel is convolved with
> its own set of filters (of size
> out_channelsin_channels\frac{\text{out\_channels}}{\text{in\_channels}}in_channelsout_channels​).

Note

The `padding` argument effectively adds `dilation * (kernel_size - 1) - padding`
amount of zero padding to both sides of the input. This is set so that
when a [`Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d) and a [`ConvTranspose1d`](torch.nn.ConvTranspose1d.html#torch.nn.ConvTranspose1d)
are initialized with same parameters, they are inverses of each other in
regard to the input and output shapes. However, when `stride > 1`,
[`Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d) maps multiple input shapes to the same output
shape. `output_padding` is provided to resolve this ambiguity by
effectively increasing the calculated output shape on one side. Note
that `output_padding` is only used to find output shape, but does
not actually add zero-padding to output.

Note

In some circumstances when using the CUDA backend with CuDNN, this operator
may select a nondeterministic algorithm to increase performance. If this is
undesirable, you can try to make the operation deterministic (potentially at
a performance cost) by setting `torch.backends.cudnn.deterministic =
True`.
Please see the notes on [Reproducibility](../notes/randomness.html) for background.

Parameters:

- **in_channels** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of channels in the input image
- **out_channels** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of channels produced by the convolution
- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Size of the convolving kernel
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - Stride of the convolution. Default: 1
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - `dilation * (kernel_size - 1) - padding` zero-padding
will be added to both sides of the input. Default: 0
- **output_padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - Additional size added to one side
of the output shape. Default: 0
- **groups** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Number of blocked connections from input channels to output channels. Default: 1
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True`, adds a learnable bias to the output. Default: `True`
- **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - Spacing between kernel elements. Default: 1

Shape:

- Input: (N,Cin,Lin)(N, C_{in}, L_{in})(N,Cin​,Lin​) or (Cin,Lin)(C_{in}, L_{in})(Cin​,Lin​)
- Output: (N,Cout,Lout)(N, C_{out}, L_{out})(N,Cout​,Lout​) or (Cout,Lout)(C_{out}, L_{out})(Cout​,Lout​), where

Lout=(Lin−1)×stride−2×padding+dilation×(kernel_size−1)+output_padding+1L_{out} = (L_{in} - 1) \times \text{stride} - 2 \times \text{padding} + \text{dilation}
 \times (\text{kernel\_size} - 1) + \text{output\_padding} + 1

Lout​=(Lin​−1)×stride−2×padding+dilation×(kernel_size−1)+output_padding+1

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - the learnable weights of the module of shape
(in_channels,out_channelsgroups,(\text{in\_channels}, \frac{\text{out\_channels}}{\text{groups}},(in_channels,groupsout_channels​,
kernel_size)\text{kernel\_size})kernel_size).
The values of these weights are sampled from
U(−k,k)\mathcal{U}(-\sqrt{k}, \sqrt{k})U(−k​,k​) where
k=groupsCout∗kernel_sizek = \frac{groups}{C_\text{out} * \text{kernel\_size}}k=Cout​∗kernel_sizegroups​
- **bias** ([*Tensor*](../tensors.html#torch.Tensor)) - the learnable bias of the module of shape (out_channels).
If `bias` is `True`, then the values of these weights are
sampled from U(−k,k)\mathcal{U}(-\sqrt{k}, \sqrt{k})U(−k​,k​) where
k=groupsCout∗kernel_sizek = \frac{groups}{C_\text{out} * \text{kernel\_size}}k=Cout​∗kernel_sizegroups​

Examples:

```
>>> # With square kernels and equal stride
>>> m = nn.ConvTranspose1d(16, 33, 3, stride=2)
>>> input = torch.randn(20, 16, 50)
>>> output = m(input)
>>> # exact output size can be also specified as an argument
>>> input = torch.randn(1, 16, 12)
>>> downsample = nn.Conv1d(16, 16, 3, stride=2, padding=1)
>>> upsample = nn.ConvTranspose1d(16, 16, 3, stride=2, padding=1)
>>> h = downsample(input)
>>> h.size()
torch.Size([1, 16, 6])
>>> output = upsample(h, output_size=input.size())
>>> output.size()
torch.Size([1, 16, 12])
```