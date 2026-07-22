# LazyConvTranspose3d

*class*torch.nn.modules.conv.LazyConvTranspose3d(*out_channels*, *kernel_size*, *stride=1*, *padding=0*, *output_padding=0*, *groups=1*, *bias=True*, *dilation=1*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/nn/modules/conv.py#L1853)

A [`torch.nn.ConvTranspose3d`](torch.nn.ConvTranspose3d.html#torch.nn.ConvTranspose3d) module with lazy initialization of the `in_channels` argument.

The `in_channels` argument of the [`ConvTranspose3d`](torch.nn.modules.conv.ConvTranspose3d.html#torch.nn.modules.conv.ConvTranspose3d) is inferred from
the `input.size(1)`.
The attributes that will be lazily initialized are weight and bias.

Check the [`torch.nn.modules.lazy.LazyModuleMixin`](torch.nn.modules.lazy.LazyModuleMixin.html#torch.nn.modules.lazy.LazyModuleMixin) for further documentation
on lazy modules and their limitations.

Parameters:

- **out_channels** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of channels produced by the convolution
- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Size of the convolving kernel
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - Stride of the convolution. Default: 1
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - `dilation * (kernel_size - 1) - padding` zero-padding
will be added to both sides of each dimension in the input. Default: 0
- **output_padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - Additional size added to one side
of each dimension in the output shape. Default: 0
- **groups** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Number of blocked connections from input channels to output channels. Default: 1
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True`, adds a learnable bias to the output. Default: `True`
- **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - Spacing between kernel elements. Default: 1

See also

[`torch.nn.ConvTranspose3d`](torch.nn.ConvTranspose3d.html#torch.nn.ConvTranspose3d) and [`torch.nn.modules.lazy.LazyModuleMixin`](torch.nn.modules.lazy.LazyModuleMixin.html#torch.nn.modules.lazy.LazyModuleMixin)

cls_to_become[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/nn/modules/conv.py#L1210)

alias of [`ConvTranspose3d`](torch.nn.modules.conv.ConvTranspose3d.html#torch.nn.modules.conv.ConvTranspose3d)