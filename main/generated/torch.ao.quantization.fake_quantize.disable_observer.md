# disable_observer

*class*torch.ao.quantization.fake_quantize.disable_observer(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/ao/quantization/fake_quantize.py#L640)

Disable observation for this module.

Disable observation for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.disable_observer)
```