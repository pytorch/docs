# disable_fake_quant

*class*torch.ao.quantization.fake_quantize.disable_fake_quant(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/ao/quantization/fake_quantize.py#L614)

Disable fake quantization for the module.

Disable fake quantization for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.disable_fake_quant)
```