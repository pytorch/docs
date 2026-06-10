# enable_observer

*class*torch.ao.quantization.fake_quantize.enable_observer(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/ao/quantization/fake_quantize.py#L653)

Enable observation for this module.

Enable observation for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.enable_observer)
```