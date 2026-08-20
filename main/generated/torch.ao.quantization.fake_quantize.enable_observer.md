# enable_observer

*class*torch.ao.quantization.fake_quantize.enable_observer(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/ao/quantization/fake_quantize.py#L653)

Enable observation for this module.

Enable observation for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.enable_observer)
```