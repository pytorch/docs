# enable_fake_quant

*class*torch.ao.quantization.fake_quantize.enable_fake_quant(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/ao/quantization/fake_quantize.py#L627)

Enable fake quantization for the module.

Enable fake quantization for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.enable_fake_quant)
```