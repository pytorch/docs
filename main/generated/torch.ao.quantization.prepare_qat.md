# prepare_qat

*class*torch.ao.quantization.prepare_qat(*model*, *mapping=None*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/12a9ea264bf805a66cd87e19e767ab23c2f59fef/torch/ao/quantization/quantize.py#L574)

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