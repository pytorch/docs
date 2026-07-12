# torch.nn.functional.pixel_unshuffle

torch.nn.functional.pixel_unshuffle(*input*, *downscale_factor*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/nn/functional.py#L4722)

Reverses the [`PixelShuffle`](torch.nn.PixelShuffle.html#torch.nn.PixelShuffle) operation by rearranging elements in a
tensor of shape (∗,C,H×r,W×r)(*, C, H \times r, W \times r)(∗,C,H×r,W×r) to a tensor of shape
(∗,C×r2,H,W)(*, C \times r^2, H, W)(∗,C×r2,H,W), where r is the `downscale_factor`.

See [`PixelUnshuffle`](torch.nn.PixelUnshuffle.html#torch.nn.PixelUnshuffle) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **downscale_factor** ([*int*](https://docs.python.org/3/library/functions.html#int)) - factor to increase spatial resolution by

Examples:

```
>>> input = torch.randn(1, 1, 12, 12)
>>> output = torch.nn.functional.pixel_unshuffle(input, 3)
>>> print(output.size())
torch.Size([1, 9, 4, 4])
```