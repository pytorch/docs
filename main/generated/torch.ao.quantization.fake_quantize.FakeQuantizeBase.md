# FakeQuantizeBase

*class*torch.ao.quantization.fake_quantize.FakeQuantizeBase[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/ao/quantization/fake_quantize.py#L70)

Base fake quantize module.

Base fake quantize module
Any fake quantize implementation should derive from this class.

Concrete fake quantize module should follow the same API. In forward, they will update
the statistics of the observed Tensor and fake quantize the input. They should also provide a
calculate_qparams function that computes the quantization parameters given
the collected statistics.