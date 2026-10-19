# activation_is_dynamically_quantized

*class*torch.ao.quantization.utils.activation_is_dynamically_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/ao/quantization/utils.py#L298)

Given a qconfig, decide if the activation needs to be
dynamically quantized or not, this includes dynamically quantizing to
quint8, qint8 and float16