# PlaceholderObserver

*class*torch.ao.quantization.observer.PlaceholderObserver(*dtype=torch.float32*, *custom_op_name=''*, *compute_dtype=None*, *quant_min=None*, *quant_max=None*, *qscheme=None*, *eps=None*, *is_dynamic=False*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/ao/quantization/observer.py#L1468)

Observer that doesn't do anything and just passes its configuration to the
quantized module's `.from_float()`.

Can be used for quantization to float16 which doesn't require determining
ranges.

Parameters:

- **dtype** - dtype argument to the quantize node needed to implement the
reference model spec.
- **quant_min** - minimum value in quantized domain (TODO: align behavior with other observers)
- **quant_max** - maximum value in quantized domain
- **custom_op_name** - (temporary) specify this observer for an operator that doesn't require any observation
(Can be used in Graph Mode Passes for special case ops).
- **compute_dtype** (*deprecated*) - if set, marks the future quantize function to use
dynamic quantization instead of static quantization.
This field is deprecated, use is_dynamic=True instead.
- **is_dynamic** - if True, the quantize function in the reference model
representation taking stats from this observer instance will
use dynamic quantization.