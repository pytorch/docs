# activation_is_int8_quantized

*class*torch.ao.quantization.utils.activation_is_int8_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/ao/quantization/utils.py#L307)

Given a qconfig, decide if the activation needs to be
quantized to int8 or not, this includes quantizing to quint8, qint8