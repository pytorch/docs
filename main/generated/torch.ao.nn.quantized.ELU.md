# ELU

*class*torch.ao.nn.quantized.ELU(*scale*, *zero_point*, *alpha=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/a483bad75086c479c263d54ad3dbf19e1fde74d8/torch/ao/nn/quantized/modules/activation.py#L89)

This is the quantized equivalent of [`ELU`](torch.nn.ELU.html#torch.nn.ELU).

Parameters:

- **scale** - quantization scale of the output tensor
- **zero_point** - quantization zero point of the output tensor
- **alpha** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) - the alpha constant