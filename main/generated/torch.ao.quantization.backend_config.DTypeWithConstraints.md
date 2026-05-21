# DTypeWithConstraints

*class*torch.ao.quantization.backend_config.DTypeWithConstraints(*dtype=None*, *quant_min_lower_bound=None*, *quant_max_upper_bound=None*, *scale_min_lower_bound=None*, *scale_max_upper_bound=None*, *scale_exact_match=None*, *zero_point_exact_match=None*)[[source]](https://github.com/pytorch/pytorch/blob/1af0b90bbfa06b98936ac35f25070579cffc8d74/torch/ao/quantization/backend_config/backend_config.py#L78)

Config for specifying additional constraints for a given dtype, such as quantization
value ranges, scale value ranges, and fixed quantization params, to be used in
[`DTypeConfig`](torch.ao.quantization.backend_config.DTypeConfig.html#torch.ao.quantization.backend_config.DTypeConfig).

The constraints currently supported are:

- quant_min_lower_bound and quant_max_upper_bound: Lower and upper
bounds for the minimum and maximum quantized values respectively. If
the QConfig's quant_min and quant_max fall outside this range,
then the QConfig will be ignored.
- scale_min_lower_bound and scale_max_upper_bound: Lower and upper
bounds for the minimum and maximum scale values respectively. If the
QConfig's minimum scale value (currently exposed as eps) falls below
the lower bound, then the QConfig will be ignored. Note that the upper
bound is currently not enforced.
- scale_exact_match and zero_point_exact_match: Exact match requirements
for scale and zero point, to be used for operators with fixed quantization
parameters such as sigmoid and tanh. If the observer specified in the QConfig
is neither FixedQParamsObserver nor FixedQParamsFakeQuantize, or if
the quantization parameters don't match, then the QConfig will be ignored.