# disable_fake_quant

*class*torch.ao.quantization.fake_quantize.disable_fake_quant(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/ao/quantization/fake_quantize.py#L614)

Disable fake quantization for the module.

Disable fake quantization for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.disable_fake_quant)
```