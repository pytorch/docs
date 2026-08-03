# ELU

*class*torch.ao.nn.quantized.ELU(*scale*, *zero_point*, *alpha=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/ao/nn/quantized/modules/activation.py#L89)

This is the quantized equivalent of [`ELU`](torch.nn.ELU.html#torch.nn.ELU).

Parameters:

- **scale** - quantization scale of the output tensor
- **zero_point** - quantization zero point of the output tensor
- **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the alpha constant