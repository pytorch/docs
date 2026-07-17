# quantize_dynamic

*class*torch.ao.quantization.quantize_dynamic(*model*, *qconfig_spec=None*, *dtype=torch.qint8*, *mapping=None*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/3fadfe4be9707a8a43a23db6e0da32dc1b507694/torch/ao/quantization/quantize.py#L483)

Converts a float model to dynamic (i.e. weights-only) quantized model.

Replaces specified modules with dynamic weight-only quantized versions and output the quantized model.

For simplest usage provide dtype argument that can be float16 or qint8. Weight-only quantization
by default is performed for layers with large weights size - i.e. Linear and RNN variants.

Fine grained control is possible with qconfig and mapping that act similarly to quantize().
If qconfig is provided, the dtype argument is ignored.

Parameters:

- **model** - input model
- **qconfig_spec** -

Either:

- A dictionary that maps from name or type of submodule to quantization
configuration, qconfig applies to all submodules of a given
module unless qconfig for the submodules are specified (when the
submodule already has qconfig attribute). Entries in the dictionary
need to be QConfig instances.
- A set of types and/or submodule names to apply dynamic quantization to,
in which case the dtype argument is used to specify the bit-width
- **inplace** - carry out model transformations in-place, the original module is mutated
- **mapping** - maps type of a submodule to a type of corresponding dynamically quantized version
with which the submodule needs to be replaced