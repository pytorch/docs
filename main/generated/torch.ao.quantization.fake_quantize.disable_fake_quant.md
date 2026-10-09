# disable_fake_quant

*class*torch.ao.quantization.fake_quantize.disable_fake_quant(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/ao/quantization/fake_quantize.py#L614)

Disable fake quantization for the module.

Disable fake quantization for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.disable_fake_quant)
```