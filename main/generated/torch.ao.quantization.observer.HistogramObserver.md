# HistogramObserver

*class*torch.ao.quantization.observer.HistogramObserver(*bins=2048*, *dtype=torch.quint8*, *qscheme=torch.per_tensor_affine*, *reduce_range=False*, *quant_min=None*, *quant_max=None*, *factory_kwargs=None*, *eps=1.1920928955078125e-07*, *is_dynamic=False*, ***, *consider_full_range=False*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/08c2d21eeac45d7bb2b95f497938e99c0250222d/torch/ao/quantization/observer.py#L987)

The module records the running histogram of tensor values along with
min/max values. `calculate_qparams` will calculate scale and zero_point.

Parameters:

- **bins** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Number of bins to use for the histogram
- **dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)) - dtype argument to the quantize node needed to implement the
reference model spec
- **qscheme** - Quantization scheme to be used
- **reduce_range** - Reduces the range of the quantized data type by 1 bit
- **eps** ([*Tensor*](../tensors.html#torch.Tensor)) - Epsilon value for float32, Defaults to torch.finfo(torch.float32).eps.
- **consider_full_range** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - Whether the min/max search may return the full observed
range. If `True`, the chosen range never has a higher estimated L2
quantization error than the full observed `[min_val, max_val]` range.
If `False` (default), the search always trims at least one histogram
bin from one end of the range, even when that increases the estimated
error, matching historical behavior.

The scale and zero point are computed as follows:

1. Create the histogram of the incoming inputs.

The histogram is computed continuously, and the ranges per bin change
with every new tensor observed.
2. Search the distribution in the histogram for optimal min/max values.

The search for the min/max values ensures the minimization of the
quantization error with respect to the floating point model.
3. Compute the scale and zero point the same way as in the

`MinMaxObserver`