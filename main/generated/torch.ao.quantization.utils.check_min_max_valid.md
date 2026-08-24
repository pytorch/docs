# check_min_max_valid

*class*torch.ao.quantization.utils.check_min_max_valid(*min_val*, *max_val*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/ao/quantization/utils.py#L414)

Checks if the given minimum and maximum values are valid, meaning that
they exist and the min value is less than the max value.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)