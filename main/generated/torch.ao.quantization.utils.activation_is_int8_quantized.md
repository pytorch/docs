# activation_is_int8_quantized

*class*torch.ao.quantization.utils.activation_is_int8_quantized(*qconfig*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/ao/quantization/utils.py#L307)

Given a qconfig, decide if the activation needs to be
quantized to int8 or not, this includes quantizing to quint8, qint8