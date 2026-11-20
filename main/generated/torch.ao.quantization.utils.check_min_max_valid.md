# check_min_max_valid

*class*torch.ao.quantization.utils.check_min_max_valid(*min_val*, *max_val*)[[source]](https://github.com/pytorch/pytorch/blob/efbc87071fdf61bd50d5dc3b315b65bd452c401d/torch/ao/quantization/utils.py#L414)

Checks if the given minimum and maximum values are valid, meaning that
they exist and the min value is less than the max value.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)