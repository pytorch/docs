# torch.nn.functional.softmin

torch.nn.functional.softmin(*input*, *dim=None*, *_stacklevel=3*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/nn/functional.py#L2143)

Apply a softmin function.

Note that Softmin(x)=Softmax(−x)\text{Softmin}(x) = \text{Softmax}(-x)Softmin(x)=Softmax(−x). See softmax definition for mathematical formula.

See [`Softmin`](torch.nn.Softmin.html#torch.nn.Softmin) for more details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - input
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - A dimension along which softmin will be computed (so every slice
along dim will sum to 1).
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is casted to `dtype` before the operation
is performed. This is useful for preventing data type overflows. Default: None.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)