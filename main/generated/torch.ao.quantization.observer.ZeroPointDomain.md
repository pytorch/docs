# ZeroPointDomain

*class*torch.ao.quantization.observer.ZeroPointDomain(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/ao/quantization/observer.py#L1660)

Enum that indicate whether zero_point is in integer domain or floating point domain

integer domain: quantized_val = (float_val / scale) (integer) + zero_point (integer)
float domain: quantized_val = (float_val - (zero_point (float) - scale * mid_point)) / scale
none domain: quantized_val = (float_val / scale)