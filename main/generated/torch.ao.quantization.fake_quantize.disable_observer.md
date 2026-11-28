# disable_observer

*class*torch.ao.quantization.fake_quantize.disable_observer(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/ao/quantization/fake_quantize.py#L640)

Disable observation for this module.

Disable observation for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.disable_observer)
```