# enable_fake_quant

*class*torch.ao.quantization.fake_quantize.enable_fake_quant(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/ao/quantization/fake_quantize.py#L627)

Enable fake quantization for the module.

Enable fake quantization for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.enable_fake_quant)
```