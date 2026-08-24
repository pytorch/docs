# enable_observer

*class*torch.ao.quantization.fake_quantize.enable_observer(*mod*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/ao/quantization/fake_quantize.py#L653)

Enable observation for this module.

Enable observation for this module, if applicable. Example usage:

```
# model is any PyTorch model
model.apply(torch.ao.quantization.enable_observer)
```