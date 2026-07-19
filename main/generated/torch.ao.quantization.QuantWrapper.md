# QuantWrapper

*class*torch.ao.quantization.QuantWrapper(*module*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/ao/quantization/stubs.py#L47)

A wrapper class that wraps the input module, adds QuantStub and
DeQuantStub and surround the call to module with call to quant and dequant
modules.

This is used by the quantization utility functions to add the quant and
dequant modules, before convert function QuantStub will just be observer,
it observes the input tensor, after convert, QuantStub
will be swapped to nnq.Quantize which does actual quantization. Similarly
for DeQuantStub.