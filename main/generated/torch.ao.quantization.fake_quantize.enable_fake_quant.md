# enable_fake_quant

*class*torch.ao.quantization.fake_quantize.enable_fake_quant(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/ao/quantization/fake_quantize.py#L627)

Enable fake quantization for the module.

Enable fake quantization for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.enable_fake_quant)
```