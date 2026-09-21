# LeakyReLU

*class*torch.ao.nn.quantized.LeakyReLU(*scale*, *zero_point*, *negative_slope=0.01*, *inplace=False*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/e1994aea9ce307fb82feeb7524ab2c5d36771e4f/torch/ao/nn/quantized/modules/activation.py#L121)

This is the quantized equivalent of [`LeakyReLU`](torch.nn.LeakyReLU.html#torch.nn.LeakyReLU).

Parameters:

- **scale** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) - quantization scale of the output tensor
- **zero_point** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - quantization zero point of the output tensor
- **negative_slope** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) - Controls the angle of the negative slope. Default: 1e-2