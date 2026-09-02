# MappingType

*class*torch.ao.quantization.observer.MappingType(*value*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/quantization/observer.py#L1636)

How floating point number is mapped to integer number

symmetric mapping means floating point range is symmetrically mapped to integer range
let's say we have floating point range (-3.5, 10.2) and integer range (-8, 7) (int4)
we'll use (-10.2, 10.2) as the range for floating point and map that to (-8, 7)
e.g. scale = (10.2 - (-10.2)) / (7 - (-8))

SYMMETRIC_NO_CLIPPING_ERR is a variant of symmetric mapping, where the scale is the max of smin
and smax, where smin = min_val_neg / quant_min, and smax = max_val_pos / quant_max. By calculating
smin and smax individually, there can be less round error on negative values, and no out-of-range
of all floating point values.

asymmetric mapping means we just directly map the floating point range to integer range,
for the above example, we will map (-3.5, 10.2) to (-8, 7) and calculate quantization parameter
based on this mapping
e.g. scale = (10.2 - (-3.5)) / (7 - (-8))