# MinMaxObserver

*class*torch.ao.quantization.observer.MinMaxObserver(*dtype=torch.quint8*, *qscheme=torch.per_tensor_affine*, *reduce_range=False*, *quant_min=None*, *quant_max=None*, *factory_kwargs=None*, *eps=1.1920928955078125e-07*, *is_dynamic=False*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/ao/quantization/observer.py#L440)

Observer module for computing the quantization parameters based on the
running min and max values.

This observer uses the tensor min/max statistics to compute the quantization
parameters. The module records the running minimum and maximum of incoming
tensors, and uses this statistic to compute the quantization parameters.

Parameters:

- **dtype** - dtype argument to the quantize node needed to implement the
reference model spec.
- **qscheme** - Quantization scheme to be used
- **reduce_range** - Reduces the range of the quantized data type by 1 bit
- **quant_min** - Minimum quantization value. If unspecified, it will follow the 8-bit setup.
- **quant_max** - Maximum quantization value. If unspecified, it will follow the 8-bit setup.
- **eps** ([*Tensor*](../tensors.html#torch.Tensor)) - Epsilon value for float32, Defaults to torch.finfo(torch.float32).eps.

Given running min/max as xminx_\text{min}xmin​ and xmaxx_\text{max}xmax​,
scale sss and zero point zzz are computed as:

The running minimum/maximum xmin/maxx_\text{min/max}xmin/max​ is computed as:

xmin={min⁡(X)if xmin=Nonemin⁡(xmin,min⁡(X))otherwisexmax={max⁡(X)if xmax=Nonemax⁡(xmax,max⁡(X))otherwise\begin{array}{ll}
x_\text{min} &= \begin{cases}
 \min(X) & \text{if~}x_\text{min} = \text{None} \\
 \min\left(x_\text{min}, \min(X)\right) & \text{otherwise}
\end{cases}\\
x_\text{max} &= \begin{cases}
 \max(X) & \text{if~}x_\text{max} = \text{None} \\
 \max\left(x_\text{max}, \max(X)\right) & \text{otherwise}
\end{cases}\\
\end{array}xmin​xmax​​={min(X)min(xmin​,min(X))​if xmin​=Noneotherwise​={max(X)max(xmax​,max(X))​if xmax​=Noneotherwise​​

where XXX is the observed tensor.

The scale sss and zero point zzz are then computed as:

if Symmetric:s=2max⁡(∣xmin∣,xmax)/(Qmax−Qmin)z={0if dtype is qint8128otherwiseOtherwise:s=(xmax−xmin)/(Qmax−Qmin)z=Qmin−round(xmin/s)\begin{aligned}
 \text{if Symmetric:}&\\
 &s = 2 \max(|x_\text{min}|, x_\text{max}) /
 \left( Q_\text{max} - Q_\text{min} \right) \\
 &z = \begin{cases}
 0 & \text{if dtype is qint8} \\
 128 & \text{otherwise}
 \end{cases}\\
 \text{Otherwise:}&\\
 &s = \left( x_\text{max} - x_\text{min} \right ) /
 \left( Q_\text{max} - Q_\text{min} \right ) \\
 &z = Q_\text{min} - \text{round}(x_\text{min} / s)
\end{aligned}if Symmetric:Otherwise:​s=2max(∣xmin​∣,xmax​)/(Qmax​−Qmin​)z={0128​if dtype is qint8otherwise​s=(xmax​−xmin​)/(Qmax​−Qmin​)z=Qmin​−round(xmin​/s)​

where QminQ_\text{min}Qmin​ and QmaxQ_\text{max}Qmax​ are the minimum and
maximum of the quantized data type.

Warning

`dtype` can only take `torch.qint8` or `torch.quint8`.

Note

If the running minimum equals to the running maximum, the scale
and zero_point are set to 1.0 and 0.

calculate_qparams()[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/ao/quantization/observer.py#L571)

Calculates the quantization parameters.

forward(*x_orig*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/ao/quantization/observer.py#L558)

Records the running minimum and maximum of `x`.

reset_min_max_vals()[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/ao/quantization/observer.py#L580)

Resets the min/max values.