# check_min_max_valid

*class*torch.ao.quantization.utils.check_min_max_valid(*min_val*, *max_val*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/ao/quantization/utils.py#L414)

Checks if the given minimum and maximum values are valid, meaning that
they exist and the min value is less than the max value.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)