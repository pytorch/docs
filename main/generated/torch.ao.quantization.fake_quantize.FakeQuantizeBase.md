# FakeQuantizeBase

*class*torch.ao.quantization.fake_quantize.FakeQuantizeBase[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/ao/quantization/fake_quantize.py#L70)

Base fake quantize module.

Base fake quantize module
Any fake quantize implementation should derive from this class.

Concrete fake quantize module should follow the same API. In forward, they will update
the statistics of the observed Tensor and fake quantize the input. They should also provide a
calculate_qparams function that computes the quantization parameters given
the collected statistics.