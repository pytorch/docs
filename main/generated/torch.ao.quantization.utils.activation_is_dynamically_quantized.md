# activation_is_dynamically_quantized

*class*torch.ao.quantization.utils.activation_is_dynamically_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/ao/quantization/utils.py#L298)

Given a qconfig, decide if the activation needs to be
dynamically quantized or not, this includes dynamically quantizing to
quint8, qint8 and float16