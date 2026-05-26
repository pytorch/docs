# torch.func.rearrange

torch.func.rearrange(*tensor*, *pattern*, ***axes_lengths*)[[source]](https://github.com/pytorch/pytorch/blob/09c9b1ec9c2e88520d11a9c64b206359e8ca912b/torch/_functorch/einops.py#L10)

A native implementation of einops.rearrange, a reader-friendly smart element reordering for multidimensional
tensors. This operation includes functionality of transpose (axes permutation), reshape (view), squeeze, unsqueeze,
stack, concatenate and other operations.

See: [https://einops.rocks/api/rearrange/](https://einops.rocks/api/rearrange/)

Parameters:

- **tensor** ([*Tensor*](../tensors.html#torch.Tensor)*or**sequence**of*[*Tensor*](../tensors.html#torch.Tensor)) - the tensor(s) to rearrange
- **pattern** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - the rearrangement pattern
- **axes_lengths** ([*int*](https://docs.python.org/3/library/functions.html#int)) - any additional length specifications for dimensions

Returns:

the rearranged tensor

Return type:

[Tensor](../tensors.html#torch.Tensor)

Examples

```
>>> from torch.func import rearrange
>>> # suppose we have a set of 32 images in "h w c" format (height-width-channel)
>>> images = torch.randn((32, 30, 40, 3))
```

```
>>> # stack along first (batch) axis, output is a single array
>>> rearrange(images, "b h w c -> b h w c").shape
torch.Size([32, 30, 40, 3])
```

```
>>> # concatenate images along height (vertical axis), 960 = 32 * 30
>>> rearrange(images, "b h w c -> (b h) w c").shape
torch.Size([960, 40, 3])
```

```
>>> # concatenated images along horizontal axis, 1280 = 32 * 40
>>> rearrange(images, "b h w c -> h (b w) c").shape
torch.Size([30, 1280, 3])
```

```
>>> # reordered axes to "b c h w" format for deep learning
>>> rearrange(images, "b h w c -> b c h w").shape
torch.Size([32, 3, 30, 40])
```

```
>>> # flattened each image into a vector, 3600 = 30 * 40 * 3
>>> rearrange(images, "b h w c -> b (c h w)").shape
torch.Size([32, 3600])
```

```
>>> # split each image into 4 smaller (top-left, top-right, bottom-left, bottom-right), 128 = 32 * 2 * 2
>>> rearrange(images, "b (h1 h) (w1 w) c -> (b h1 w1) h w c", h1=2, w1=2).shape
torch.Size([128, 15, 20, 3])
```

```
>>> # space-to-depth operation
>>> rearrange(images, "b (h h1) (w w1) c -> b h w (c h1 w1)", h1=2, w1=2).shape
torch.Size([32, 15, 20, 12])
```