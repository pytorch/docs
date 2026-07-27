# activation_is_statically_quantized

*class*torch.ao.quantization.utils.activation_is_statically_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/94de2113ebf2891e498dd58ed1a16fedac39b5c6/torch/ao/quantization/utils.py#L280)

Given a qconfig, decide if the activation needs to be
quantized or not, this includes quantizing to quint8, qint8 and qint32 and float16