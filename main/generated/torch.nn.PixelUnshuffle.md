# PixelUnshuffle

*class*torch.nn.PixelUnshuffle(*downscale_factor*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/nn/modules/pixelshuffle.py#L71)

Reverse the PixelShuffle operation.

Reverses the [`PixelShuffle`](torch.nn.PixelShuffle.html#torch.nn.PixelShuffle) operation by rearranging elements
in a tensor of shape (∗,C,H×r,W×r)(*, C, H \times r, W \times r)(∗,C,H×r,W×r) to a tensor of shape
(∗,C×r2,H,W)(*, C \times r^2, H, W)(∗,C×r2,H,W), where r is a downscale factor.

See the paper:
[Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network](https://arxiv.org/abs/1609.05158)
by Shi et al. (2016) for more details.

Parameters:

**downscale_factor** ([*int*](https://docs.python.org/3/library/functions.html#int)) - factor to decrease spatial resolution by

Shape:

- Input: (∗,Cin,Hin,Win)(*, C_{in}, H_{in}, W_{in})(∗,Cin​,Hin​,Win​), where * is zero or more batch dimensions
- Output: (∗,Cout,Hout,Wout)(*, C_{out}, H_{out}, W_{out})(∗,Cout​,Hout​,Wout​), where

Cout=Cin×downscale_factor2C_{out} = C_{in} \times \text{downscale\_factor}^2

Cout​=Cin​×downscale_factor2
Hout=Hin÷downscale_factorH_{out} = H_{in} \div \text{downscale\_factor}

Hout​=Hin​÷downscale_factor
Wout=Win÷downscale_factorW_{out} = W_{in} \div \text{downscale\_factor}

Wout​=Win​÷downscale_factor

Examples:

```
>>> pixel_unshuffle = nn.PixelUnshuffle(3)
>>> input = torch.randn(1, 1, 12, 12)
>>> output = pixel_unshuffle(input)
>>> print(output.size())
torch.Size([1, 9, 4, 4])
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/nn/modules/pixelshuffle.py#L123)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/nn/modules/pixelshuffle.py#L117)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)