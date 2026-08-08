# ELU

*class*torch.ao.nn.quantized.ELU(*scale*, *zero_point*, *alpha=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/ao/nn/quantized/modules/activation.py#L89)

This is the quantized equivalent of [`ELU`](torch.nn.ELU.html#torch.nn.ELU).

Parameters:

- **scale** - quantization scale of the output tensor
- **zero_point** - quantization zero point of the output tensor
- **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the alpha constant