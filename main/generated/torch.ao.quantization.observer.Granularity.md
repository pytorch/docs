# Granularity

*class*torch.ao.quantization.observer.Granularity[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/ao/quantization/observer.py#L1689)

Base class for representing the granularity of quantization.

This class serves as a parent for specific granularity types used in
quantization operations, such as per-tensor or per-axis quantization.