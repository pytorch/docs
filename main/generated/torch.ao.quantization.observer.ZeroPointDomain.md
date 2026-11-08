# ZeroPointDomain

*class*torch.ao.quantization.observer.ZeroPointDomain(*value*, *names=None*, ***, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/ao/quantization/observer.py#L1683)

Enum that indicate whether zero_point is in integer domain or floating point domain

integer domain: quantized_val = (float_val / scale) (integer) + zero_point (integer)
float domain: quantized_val = (float_val - (zero_point (float) - scale * mid_point)) / scale
none domain: quantized_val = (float_val / scale)