# QuantWrapper

*class*torch.ao.quantization.QuantWrapper(*module*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/ao/quantization/stubs.py#L47)

A wrapper class that wraps the input module, adds QuantStub and
DeQuantStub and surrounds the call to module with call to quant and dequant
modules.

This is used by the quantization utility functions to add the quant and
dequant modules, before convert function QuantStub will just be observer,
it observes the input tensor, after convert, QuantStub
will be swapped to nnq.Quantize which does actual quantization. Similarly
for DeQuantStub.