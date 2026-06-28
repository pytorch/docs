# calculate_qmin_qmax

*class*torch.ao.quantization.utils.calculate_qmin_qmax(*quant_min*, *quant_max*, *has_customized_qrange*, *dtype*, *reduce_range*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/ao/quantization/utils.py#L445)

Calculates actual qmin and qmax based on the quantization range,
observer datatype and if range is reduced.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]