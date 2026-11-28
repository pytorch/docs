# Granularity

*class*torch.ao.quantization.observer.Granularity[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/ao/quantization/observer.py#L1712)

Base class for representing the granularity of quantization.

This class serves as a parent for specific granularity types used in
quantization operations, such as per-tensor or per-axis quantization.