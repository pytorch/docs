# calculate_qmin_qmax

*class*torch.ao.quantization.utils.calculate_qmin_qmax(*quant_min*, *quant_max*, *has_customized_qrange*, *dtype*, *reduce_range*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/ao/quantization/utils.py#L445)

Calculates actual qmin and qmax based on the quantization range,
observer datatype and if range is reduced.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]