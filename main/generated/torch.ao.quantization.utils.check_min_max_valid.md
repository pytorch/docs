# check_min_max_valid

*class*torch.ao.quantization.utils.check_min_max_valid(*min_val*, *max_val*)[[source]](https://github.com/pytorch/pytorch/blob/09c9b1ec9c2e88520d11a9c64b206359e8ca912b/torch/ao/quantization/utils.py#L414)

Checks if the given minimum and maximum values are valid, meaning that
they exist and the min value is less than the max value.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)