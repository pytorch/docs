# torch.channel_shuffle

torch.channel_shuffle(*input*, *groups*) → [Tensor](../tensors.html#torch.Tensor)

Divide the channels in a tensor of shape (∗,C,H,W)(*, C , H, W)(∗,C,H,W)
into g groups and rearrange them as (∗,Cg,g,H,W)(*, C \frac g, g, H, W)(∗,C,g​g,H,W),
while keeping the original tensor shape.

See [`ChannelShuffle`](torch.nn.ChannelShuffle.html#torch.nn.ChannelShuffle) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **groups** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of groups to divide channels in and rearrange.

Examples:

```
>>> input = torch.randn(1, 4, 2, 2)
>>> print(input)
[[[[1, 2],
 [3, 4]],
 [[5, 6],
 [7, 8]],
 [[9, 10],
 [11, 12]],
 [[13, 14],
 [15, 16]],
 ]]
>>> output = torch.nn.functional.channel_shuffle(input, 2)
>>> print(output)
[[[[1, 2],
 [3, 4]],
 [[9, 10],
 [11, 12]],
 [[5, 6],
 [7, 8]],
 [[13, 14],
 [15, 16]],
 ]]
```