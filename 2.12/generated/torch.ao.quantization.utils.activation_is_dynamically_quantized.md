# activation_is_dynamically_quantized

*class*torch.ao.quantization.utils.activation_is_dynamically_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/ao/quantization/utils.py#L295)

Given a qconfig, decide if the activation needs to be
dynamically quantized or not, this includes dynamically quantizing to
quint8, qint8 and float16