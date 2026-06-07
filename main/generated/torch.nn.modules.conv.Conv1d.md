# Conv1d

*class*torch.nn.modules.conv.Conv1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/nn/modules/conv.py#L225)

Applies a 1D convolution over an input signal composed of several input
planes.

In the simplest case, the output value of the layer with input size
(N,Cin,L)(N, C_{\text{in}}, L)(N,Cin​,L) and output (N,Cout,Lout)(N, C_{\text{out}}, L_{\text{out}})(N,Cout​,Lout​) can be
precisely described as:

out(Ni,Coutj)=bias(Coutj)+∑k=0Cin−1weight(Coutj,k)⋆input(Ni,k)\text{out}(N_i, C_{\text{out}_j}) = \text{bias}(C_{\text{out}_j}) +
\sum_{k = 0}^{C_{in} - 1} \text{weight}(C_{\text{out}_j}, k)
\star \text{input}(N_i, k)

out(Ni​,Coutj​​)=bias(Coutj​​)+k=0∑Cin​−1​weight(Coutj​​,k)⋆input(Ni​,k)

where ⋆\star⋆ is the valid [cross-correlation](https://en.wikipedia.org/wiki/Cross-correlation) operator,
NNN is a batch size, CCC denotes a number of channels,
LLL is a length of signal sequence.

This module supports [TensorFloat32](../notes/cuda.html#tf32-on-ampere).

On certain ROCm devices, when using float16 inputs this module will use [different precision](../notes/numerical_accuracy.html#fp16-on-mi200) for backward.

- `stride` controls the stride for the cross-correlation, a single
number or a one-element tuple.
- `padding` controls the amount of padding applied to the input. It
can be either a string {'valid', 'same'} or a tuple of ints giving the
amount of implicit padding applied on both sides.
- `dilation` controls the spacing between the kernel points; also
known as the à trous algorithm. It is harder to describe, but this [link](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md)
has a nice visualization of what `dilation` does.
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

When groups == in_channels and out_channels == K * in_channels,
where K is a positive integer, this operation is also known as a "depthwise convolution".

In other words, for an input of size (N,Cin,Lin)(N, C_{in}, L_{in})(N,Cin​,Lin​),
a depthwise convolution with a depthwise multiplier K can be performed with the arguments
(Cin=Cin,Cout=Cin×K,...,groups=Cin)(C_\text{in}=C_\text{in}, C_\text{out}=C_\text{in} \times \text{K}, ..., \text{groups}=C_\text{in})(Cin​=Cin​,Cout​=Cin​×K,...,groups=Cin​).

Note

In some circumstances when given tensors on a CUDA device and using CuDNN, this operator may select a nondeterministic algorithm to increase performance. If this is undesirable, you can try to make the operation deterministic (potentially at a performance cost) by setting `torch.backends.cudnn.deterministic = True`. See [Reproducibility](../notes/randomness.html) for more information.

Note

`padding='valid'` is the same as no padding. `padding='same'` pads
the input so the output has the shape as the input. However, this mode
doesn't support any stride values other than 1.

Note

This module supports complex data types i.e. `complex32, complex64, complex128`.

Parameters:

- **in_channels** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of channels in the input image
- **out_channels** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of channels produced by the convolution
- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Size of the convolving kernel
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - Stride of the convolution. Default: 1
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Padding added to both sides of
the input. Default: 0
- **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - Spacing between kernel
elements. Default: 1
- **groups** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Number of blocked connections from input
channels to output channels. Default: 1
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True`, adds a learnable bias to the
output. Default: `True`
- **padding_mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - `'zeros'`, `'reflect'`,
`'replicate'` or `'circular'`. Default: `'zeros'`

Shape:

- Input: (N,Cin,Lin)(N, C_{in}, L_{in})(N,Cin​,Lin​) or (Cin,Lin)(C_{in}, L_{in})(Cin​,Lin​)
- Output: (N,Cout,Lout)(N, C_{out}, L_{out})(N,Cout​,Lout​) or (Cout,Lout)(C_{out}, L_{out})(Cout​,Lout​), where

Lout=⌊Lin+2×padding−dilation×(kernel_size−1)−1stride+1⌋L_{out} = \left\lfloor\frac{L_{in} + 2 \times \text{padding} - \text{dilation}
 \times (\text{kernel\_size} - 1) - 1}{\text{stride}} + 1\right\rfloor

Lout​=⌊strideLin​+2×padding−dilation×(kernel_size−1)−1​+1⌋

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - the learnable weights of the module of shape
(out_channels,in_channelsgroups,kernel_size)(\text{out\_channels},
\frac{\text{in\_channels}}{\text{groups}}, \text{kernel\_size})(out_channels,groupsin_channels​,kernel_size).
The values of these weights are sampled from
U(−k,k)\mathcal{U}(-\sqrt{k}, \sqrt{k})U(−k​,k​) where
k=groupsCin∗kernel_sizek = \frac{groups}{C_\text{in} * \text{kernel\_size}}k=Cin​∗kernel_sizegroups​
- **bias** ([*Tensor*](../tensors.html#torch.Tensor)) - the learnable bias of the module of shape
(out_channels). If `bias` is `True`, then the values of these weights are
sampled from U(−k,k)\mathcal{U}(-\sqrt{k}, \sqrt{k})U(−k​,k​) where
k=groupsCin∗kernel_sizek = \frac{groups}{C_\text{in} * \text{kernel\_size}}k=Cin​∗kernel_sizegroups​

Examples:

```
>>> m = nn.Conv1d(16, 33, 3, stride=2)
>>> input = torch.randn(20, 16, 50)
>>> output = m(input)
```