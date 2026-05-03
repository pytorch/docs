# swap_module

*class*torch.ao.quantization.swap_module(*mod*, *mapping*, *custom_module_class_mapping*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/ao/quantization/quantize.py#L744)

Swaps the module if it has a quantized counterpart and it has an
observer attached.

Parameters:

- **mod** - input module
- **mapping** - a dictionary that maps from nn module to nnq module

Returns:

The corresponding quantized module of mod