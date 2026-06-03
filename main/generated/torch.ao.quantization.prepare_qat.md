# prepare_qat

*class*torch.ao.quantization.prepare_qat(*model*, *mapping=None*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/ao/quantization/quantize.py#L574)

Prepares a copy of the model for quantization calibration or
quantization-aware training and converts it to quantized version.

Quantization configuration should be assigned preemptively
to individual submodules in .qconfig attribute.

Parameters:

- **model** - input model to be modified in-place
- **mapping** - dictionary that maps float modules to quantized modules to be
replaced.
- **inplace** - carry out model transformations in-place, the original module
is mutated