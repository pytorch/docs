# activation_is_statically_quantized

*class*torch.ao.quantization.utils.activation_is_statically_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/ao/quantization/utils.py#L280)

Given a qconfig, decide if the activation needs to be
quantized or not, this includes quantizing to quint8, qint8 and qint32 and float16