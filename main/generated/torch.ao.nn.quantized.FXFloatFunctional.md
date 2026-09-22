# FXFloatFunctional

*class*torch.ao.nn.quantized.FXFloatFunctional(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/ao/nn/quantized/modules/functional_modules.py#L101)

module to replace FloatFunctional module before FX graph mode quantization,
since activation_post_process will be inserted in top level module directly

Valid operation names:

- add
- cat
- mul
- add_relu
- add_scalar
- mul_scalar