# MovingAverageMinMaxObserver

*class*torch.ao.quantization.observer.MovingAverageMinMaxObserver(*averaging_constant=0.01*, *dtype=torch.quint8*, *qscheme=torch.per_tensor_affine*, *reduce_range=False*, *quant_min=None*, *quant_max=None*, *eps=1.1920928955078125e-07*, *is_dynamic=False*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/ao/quantization/observer.py#L587)

Observer module for computing the quantization parameters based on the
moving average of the min and max values.

This observer computes the quantization parameters based on the moving
averages of minimums and maximums of the incoming tensors. The module
records the average minimum and maximum of incoming tensors, and uses this
statistic to compute the quantization parameters.

Parameters:

- **averaging_constant** - Averaging constant for min/max.
- **dtype** - dtype argument to the quantize node needed to implement the
reference model spec.
- **qscheme** - Quantization scheme to be used
- **reduce_range** - Reduces the range of the quantized data type by 1 bit
- **quant_min** - Minimum quantization value. If unspecified, it will follow the 8-bit setup.
- **quant_max** - Maximum quantization value. If unspecified, it will follow the 8-bit setup.
- **eps** ([*Tensor*](../tensors.html#torch.Tensor)) - Epsilon value for float32, Defaults to torch.finfo(torch.float32).eps.

The moving average min/max is computed as follows

xmin={min⁡(X)if xmin=None(1−c)xmin+cmin⁡(X)otherwisexmax={max⁡(X)if xmax=None(1−c)xmax+cmax⁡(X)otherwise\begin{array}{ll}
 x_\text{min} = \begin{cases}
 \min(X) & \text{if~}x_\text{min} = \text{None} \\
 (1 - c) x_\text{min} + c \min(X) & \text{otherwise}
 \end{cases}\\
 x_\text{max} = \begin{cases}
 \max(X) & \text{if~}x_\text{max} = \text{None} \\
 (1 - c) x_\text{max} + c \max(X) & \text{otherwise}
 \end{cases}\\
\end{array}xmin​={min(X)(1−c)xmin​+cmin(X)​if xmin​=Noneotherwise​xmax​={max(X)(1−c)xmax​+cmax(X)​if xmax​=Noneotherwise​​

where xmin/maxx_\text{min/max}xmin/max​ is the running average min/max, XXX
is the incoming tensor, and ccc is the `averaging_constant`.

The scale and zero point are then computed as in
[`MinMaxObserver`](torch.ao.quantization.observer.MinMaxObserver.html#torch.ao.quantization.observer.MinMaxObserver).

Note

Only works with `torch.per_tensor_affine` quantization scheme.

Note

If the running minimum equals to the running maximum, the scale
and zero_point are set to 1.0 and 0.