# activation_is_int8_quantized

*class*torch.ao.quantization.utils.activation_is_int8_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/84e524623ea4754a748936bf1ba6ecaaa92c3ae6/torch/ao/quantization/utils.py#L307)

Given a qconfig, decide if the activation needs to be
quantized to int8 or not, this includes quantizing to quint8, qint8