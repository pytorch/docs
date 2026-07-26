# disable_observer

*class*torch.ao.quantization.fake_quantize.disable_observer(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/ao/quantization/fake_quantize.py#L640)

Disable observation for this module.

Disable observation for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.disable_observer)
```