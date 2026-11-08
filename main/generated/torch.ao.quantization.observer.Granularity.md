# Granularity

*class*torch.ao.quantization.observer.Granularity[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/ao/quantization/observer.py#L1712)

Base class for representing the granularity of quantization.

This class serves as a parent for specific granularity types used in
quantization operations, such as per-tensor or per-axis quantization.