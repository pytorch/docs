# activation_is_dynamically_quantized

*class*torch.ao.quantization.utils.activation_is_dynamically_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/ao/quantization/utils.py#L298)

Given a qconfig, decide if the activation needs to be
dynamically quantized or not, this includes dynamically quantizing to
quint8, qint8 and float16