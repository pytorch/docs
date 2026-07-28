# FXFloatFunctional

*class*torch.ao.nn.quantized.FXFloatFunctional(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/b7ee7397ead012835c2d80ee53f64800630b1ab9/torch/ao/nn/quantized/modules/functional_modules.py#L101)

module to replace FloatFunctional module before FX graph mode quantization,
since activation_post_process will be inserted in top level module directly

Valid operation names:

- add
- cat
- mul
- add_relu
- add_scalar
- mul_scalar