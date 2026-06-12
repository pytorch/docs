# activation_is_dynamically_quantized

*class*torch.ao.quantization.utils.activation_is_dynamically_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/ao/quantization/utils.py#L298)

Given a qconfig, decide if the activation needs to be
dynamically quantized or not, this includes dynamically quantizing to
quint8, qint8 and float16