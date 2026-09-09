# torch.nn.functional.pixel_shuffle

torch.nn.functional.pixel_shuffle(*input*, *upscale_factor*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/c712ec6ebb4ecd2838e2cafb0bbc7a3c5acfe668/torch/nn/functional.py#L4697)

Rearranges elements in a tensor of shape (∗,C×r2,H,W)(*, C \times r^2, H, W)(∗,C×r2,H,W) to a
tensor of shape (∗,C,H×r,W×r)(*, C, H \times r, W \times r)(∗,C,H×r,W×r), where r is the `upscale_factor`.

See [`PixelShuffle`](torch.nn.PixelShuffle.html#torch.nn.PixelShuffle) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **upscale_factor** ([*int*](https://docs.python.org/3/library/functions.html#int)) - factor to increase spatial resolution by

Examples:

```
>>> input = torch.randn(1, 9, 4, 4)
>>> output = torch.nn.functional.pixel_shuffle(input, 3)
>>> print(output.size())
torch.Size([1, 1, 12, 12])
```