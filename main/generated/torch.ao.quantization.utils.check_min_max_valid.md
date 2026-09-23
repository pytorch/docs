# check_min_max_valid

*class*torch.ao.quantization.utils.check_min_max_valid(*min_val*, *max_val*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/ao/quantization/utils.py#L414)

Checks if the given minimum and maximum values are valid, meaning that
they exist and the min value is less than the max value.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)