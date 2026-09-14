# calculate_qmin_qmax

*class*torch.ao.quantization.utils.calculate_qmin_qmax(*quant_min*, *quant_max*, *has_customized_qrange*, *dtype*, *reduce_range*)[[source]](https://github.com/pytorch/pytorch/blob/b8bd7cf750ea02a2390d8a5440261e2c6ed5ddc7/torch/ao/quantization/utils.py#L445)

Calculates actual qmin and qmax based on the quantization range,
observer datatype and if range is reduced.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), [int](https://docs.python.org/3/builtins/functions.html#int)]