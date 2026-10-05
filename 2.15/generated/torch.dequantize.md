# dequantize

*class*torch.dequantize(*tensor*)

Returns an fp32 Tensor by dequantizing a quantized Tensor

Parameters:

**tensor** ([*Tensor*](../tensors.html#torch.Tensor)) - A quantized Tensor

dequantize(*tensors*) → sequence of Tensors

Given a list of quantized Tensors, dequantize them and return a list of fp32 Tensors

Parameters:

**tensors** (*sequence**of**Tensors*) - A list of quantized Tensors