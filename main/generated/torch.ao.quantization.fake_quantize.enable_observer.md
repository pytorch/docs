# enable_observer

*class*torch.ao.quantization.fake_quantize.enable_observer(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/ao/quantization/fake_quantize.py#L653)

Enable observation for this module.

Enable observation for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.enable_observer)
```