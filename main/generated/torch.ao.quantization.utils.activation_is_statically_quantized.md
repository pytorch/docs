# activation_is_statically_quantized

*class*torch.ao.quantization.utils.activation_is_statically_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/ao/quantization/utils.py#L280)

Given a qconfig, decide if the activation needs to be
quantized or not, this includes quantizing to quint8, qint8 and qint32 and float16