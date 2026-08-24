# Granularity

*class*torch.ao.quantization.observer.Granularity[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/ao/quantization/observer.py#L1689)

Base class for representing the granularity of quantization.

This class serves as a parent for specific granularity types used in
quantization operations, such as per-tensor or per-axis quantization.