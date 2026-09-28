# ZeroPointDomain

*class*torch.ao.quantization.observer.ZeroPointDomain(*value*, *names=None*, ***, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[[source]](https://github.com/pytorch/pytorch/blob/2e9b4aff8d49b22bbebf288ccbf63983c51e45f0/torch/ao/quantization/observer.py#L1660)

Enum that indicate whether zero_point is in integer domain or floating point domain

integer domain: quantized_val = (float_val / scale) (integer) + zero_point (integer)
float domain: quantized_val = (float_val - (zero_point (float) - scale * mid_point)) / scale
none domain: quantized_val = (float_val / scale)