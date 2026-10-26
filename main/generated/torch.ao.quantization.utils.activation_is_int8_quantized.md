# activation_is_int8_quantized

*class*torch.ao.quantization.utils.activation_is_int8_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/b43489ea06ed9a3bb80dbbd18300f8b0ef6f56a1/torch/ao/quantization/utils.py#L307)

Given a qconfig, decide if the activation needs to be
quantized to int8 or not, this includes quantizing to quint8, qint8