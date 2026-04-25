# QuantWrapper

*class*torch.ao.quantization.QuantWrapper(*module*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/ao/quantization/stubs.py#L47)

A wrapper class that wraps the input module, adds QuantStub and
DeQuantStub and surround the call to module with call to quant and dequant
modules.

This is used by the quantization utility functions to add the quant and
dequant modules, before convert function QuantStub will just be observer,
it observes the input tensor, after convert, QuantStub
will be swapped to nnq.Quantize which does actual quantization. Similarly
for DeQuantStub.