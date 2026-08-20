# disable_observer

*class*torch.ao.quantization.fake_quantize.disable_observer(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/ao/quantization/fake_quantize.py#L640)

Disable observation for this module.

Disable observation for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.disable_observer)
```