# torch.nn.functional.softmin

torch.nn.functional.softmin(*input*, *dim=None*, *_stacklevel=3*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/nn/functional.py#L2115)

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