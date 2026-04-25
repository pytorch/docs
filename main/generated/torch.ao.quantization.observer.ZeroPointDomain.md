# ZeroPointDomain

*class*torch.ao.quantization.observer.ZeroPointDomain(*value*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/ao/quantization/observer.py#L1771)

Enum that indicate whether zero_point is in integer domain or floating point domain

integer domain: quantized_val = (float_val / scale) (integer) + zero_point (integer)
float domain: quantized_val = (float_val - (zero_point (float) - scale * mid_point)) / scale
none domain: quantized_val = (float_val / scale)