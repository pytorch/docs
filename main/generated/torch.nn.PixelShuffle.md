# PixelShuffle

*class*torch.nn.PixelShuffle(*upscale_factor*)[[source]](https://github.com/pytorch/pytorch/blob/c8f2d26abd0de59995af555e80c82ca1221bc21b/torch/nn/modules/pixelshuffle.py#L10)

Rearrange elements in a tensor according to an upscaling factor.

Rearranges elements in a tensor of shape (∗,C×r2,H,W)(*, C \times r^2, H, W)(∗,C×r2,H,W)
to a tensor of shape (∗,C,H×r,W×r)(*, C, H \times r, W \times r)(∗,C,H×r,W×r), where r is an upscale factor.

This is useful for implementing efficient sub-pixel convolution
with a stride of 1/r1/r1/r.

See the paper:
[Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network](https://arxiv.org/abs/1609.05158)
by Shi et al. (2016) for more details.

Parameters:

**upscale_factor** ([*int*](https://docs.python.org/3/library/functions.html#int)) - factor to increase spatial resolution by

Shape:

- Input: (∗,Cin,Hin,Win)(*, C_{in}, H_{in}, W_{in})(∗,Cin​,Hin​,Win​), where * is zero or more batch dimensions
- Output: (∗,Cout,Hout,Wout)(*, C_{out}, H_{out}, W_{out})(∗,Cout​,Hout​,Wout​), where

Cout=Cin÷upscale_factor2C_{out} = C_{in} \div \text{upscale\_factor}^2

Cout​=Cin​÷upscale_factor2
Hout=Hin×upscale_factorH_{out} = H_{in} \times \text{upscale\_factor}

Hout​=Hin​×upscale_factor
Wout=Win×upscale_factorW_{out} = W_{in} \times \text{upscale\_factor}

Wout​=Win​×upscale_factor

Examples:

```
>>> pixel_shuffle = nn.PixelShuffle(3)
>>> input = torch.randn(1, 9, 4, 4)
>>> output = pixel_shuffle(input)
>>> print(output.size())
torch.Size([1, 1, 12, 12])
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/c8f2d26abd0de59995af555e80c82ca1221bc21b/torch/nn/modules/pixelshuffle.py#L64)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/c8f2d26abd0de59995af555e80c82ca1221bc21b/torch/nn/modules/pixelshuffle.py#L58)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)