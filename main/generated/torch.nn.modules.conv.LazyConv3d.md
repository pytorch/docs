# LazyConv3d

*class*torch.nn.modules.conv.LazyConv3d(*out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/55dfacc69b3a9156f68cfe07b61553e4bdc7de29/torch/nn/modules/conv.py#L1636)

A [`torch.nn.Conv3d`](torch.nn.Conv3d.html#torch.nn.Conv3d) module with lazy initialization of the `in_channels` argument.

The `in_channels` argument of the [`Conv3d`](torch.nn.modules.conv.Conv3d.html#torch.nn.modules.conv.Conv3d) that is inferred from
the `input.size(1)`.
The attributes that will be lazily initialized are weight and bias.

Check the [`torch.nn.modules.lazy.LazyModuleMixin`](torch.nn.modules.lazy.LazyModuleMixin.html#torch.nn.modules.lazy.LazyModuleMixin) for further documentation
on lazy modules and their limitations.

Parameters:

- **out_channels** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of channels produced by the convolution
- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Size of the convolving kernel
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - Stride of the convolution. Default: 1
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - Zero-padding added to both sides of
the input. Default: 0
- **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - Spacing between kernel
elements. Default: 1
- **groups** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Number of blocked connections from input
channels to output channels. Default: 1
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True`, adds a learnable bias to the
output. Default: `True`
- **padding_mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - `'zeros'`, `'reflect'`,
`'replicate'` or `'circular'`. Default: `'zeros'`

See also

[`torch.nn.Conv3d`](torch.nn.Conv3d.html#torch.nn.Conv3d) and [`torch.nn.modules.lazy.LazyModuleMixin`](torch.nn.modules.lazy.LazyModuleMixin.html#torch.nn.modules.lazy.LazyModuleMixin)

cls_to_become[[source]](https://github.com/pytorch/pytorch/blob/55dfacc69b3a9156f68cfe07b61553e4bdc7de29/torch/nn/modules/conv.py#L568)

alias of [`Conv3d`](torch.nn.modules.conv.Conv3d.html#torch.nn.modules.conv.Conv3d)