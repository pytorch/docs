# Granularity

*class*torch.ao.quantization.observer.Granularity[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/ao/quantization/observer.py#L1689)

Base class for representing the granularity of quantization.

This class serves as a parent for specific granularity types used in
quantization operations, such as per-tensor or per-axis quantization.