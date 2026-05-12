# FXFloatFunctional

*class*torch.ao.nn.quantized.FXFloatFunctional(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/ao/nn/quantized/modules/functional_modules.py#L101)

module to replace FloatFunctional module before FX graph mode quantization,
since activation_post_process will be inserted in top level module directly

Valid operation names:

- add
- cat
- mul
- add_relu
- add_scalar
- mul_scalar