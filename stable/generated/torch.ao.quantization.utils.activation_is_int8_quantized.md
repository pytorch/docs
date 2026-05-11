# activation_is_int8_quantized

*class*torch.ao.quantization.utils.activation_is_int8_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/ao/quantization/utils.py#L304)

Given a qconfig, decide if the activation needs to be
quantized to int8 or not, this includes quantizing to quint8, qint8