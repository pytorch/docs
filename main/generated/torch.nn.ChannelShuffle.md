# ChannelShuffle

*class*torch.nn.ChannelShuffle(*groups*)[[source]](https://github.com/pytorch/pytorch/blob/5cd392bfe432d57e7beb9ab67037ddc0fcc01205/torch/nn/modules/channelshuffle.py#L10)

Divides and rearranges the channels in a tensor.

This operation divides the channels in a tensor of shape (N,C,∗)(N, C, *)(N,C,∗)
into g groups as (N,Cg,g,∗)(N, \frac{C}{g}, g, *)(N,gC​,g,∗) and shuffles them,
while retaining the original tensor shape in the final output.

Parameters:

**groups** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of groups to divide channels in.

Examples:

```
>>> channel_shuffle = nn.ChannelShuffle(2)
>>> input = torch.arange(1, 17, dtype=torch.float32).view(1, 4, 2, 2)
>>> input
tensor([[[[ 1., 2.],
 [ 3., 4.]],
 [[ 5., 6.],
 [ 7., 8.]],
 [[ 9., 10.],
 [11., 12.]],
 [[13., 14.],
 [15., 16.]]]])
>>> output = channel_shuffle(input)
>>> output
tensor([[[[ 1., 2.],
 [ 3., 4.]],
 [[ 9., 10.],
 [11., 12.]],
 [[ 5., 6.],
 [ 7., 8.]],
 [[13., 14.],
 [15., 16.]]]])
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/5cd392bfe432d57e7beb9ab67037ddc0fcc01205/torch/nn/modules/channelshuffle.py#L58)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/5cd392bfe432d57e7beb9ab67037ddc0fcc01205/torch/nn/modules/channelshuffle.py#L52)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)