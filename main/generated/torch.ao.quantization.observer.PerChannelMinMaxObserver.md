# PerChannelMinMaxObserver

*class*torch.ao.quantization.observer.PerChannelMinMaxObserver(*ch_axis=0*, *dtype=torch.quint8*, *qscheme=torch.per_channel_affine*, *reduce_range=False*, *quant_min=None*, *quant_max=None*, *factory_kwargs=None*, *eps=1.1920928955078125e-07*, *is_dynamic=False*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/411c8477fa2478b2318f3823d57cf684a3a1f389/torch/ao/quantization/observer.py#L686)

Observer module for computing the quantization parameters based on the
running per channel min and max values.

This observer uses the tensor min/max statistics to compute the per channel
quantization parameters. The module records the running minimum and maximum
of incoming tensors, and uses this statistic to compute the quantization
parameters.

Parameters:

- **ch_axis** - Channel axis
- **dtype** - dtype argument to the quantize node needed to implement the
reference model spec.
- **qscheme** - Quantization scheme to be used
- **reduce_range** - Reduces the range of the quantized data type by 1 bit
- **quant_min** - Minimum quantization value. If unspecified, it will follow the 8-bit setup.
- **quant_max** - Maximum quantization value. If unspecified, it will follow the 8-bit setup.
- **eps** ([*Tensor*](../tensors.html#torch.Tensor)) - Epsilon value for float32, Defaults to torch.finfo(torch.float32).eps.

The quantization parameters are computed the same way as in
[`MinMaxObserver`](torch.ao.quantization.observer.MinMaxObserver.html#torch.ao.quantization.observer.MinMaxObserver), with the difference
that the running min/max values are stored per channel.
Scales and zero points are thus computed per channel as well.

Note

If the running minimum equals to the running maximum, the scales
and zero_points are set to 1.0 and 0.

reset_min_max_vals()[[source]](https://github.com/pytorch/pytorch/blob/411c8477fa2478b2318f3823d57cf684a3a1f389/torch/ao/quantization/observer.py#L883)

Resets the min/max values.