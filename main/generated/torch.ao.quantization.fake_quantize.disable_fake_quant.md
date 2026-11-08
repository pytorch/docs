# disable_fake_quant

*class*torch.ao.quantization.fake_quantize.disable_fake_quant(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/ao/quantization/fake_quantize.py#L614)

Disable fake quantization for the module.

Disable fake quantization for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.disable_fake_quant)
```