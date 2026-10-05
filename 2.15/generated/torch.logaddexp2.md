# torch.logaddexp2

torch.logaddexp2(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Logarithm of the sum of exponentiations of the inputs in base-2.

Calculates pointwise log⁡2(2x+2y)\log_2\left(2^x + 2^y\right)log2​(2x+2y). See
[`torch.logaddexp()`](torch.logaddexp.html#torch.logaddexp) for more details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the second input tensor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.