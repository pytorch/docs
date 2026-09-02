# disable_fake_quant

*class*torch.ao.quantization.fake_quantize.disable_fake_quant(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/quantization/fake_quantize.py#L614)

Disable fake quantization for the module.

Disable fake quantization for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.disable_fake_quant)
```