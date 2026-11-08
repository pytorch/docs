# disable_observer

*class*torch.ao.quantization.fake_quantize.disable_observer(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/ao/quantization/fake_quantize.py#L640)

Disable observation for this module.

Disable observation for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.disable_observer)
```