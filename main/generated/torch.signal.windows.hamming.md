# torch.signal.windows.hamming

torch.signal.windows.hamming(*M*, ***, *sym=True*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*)[[source]](https://github.com/pytorch/pytorch/blob/dff44973f3eba04a92de8499c17cd237997140f2/torch/signal/windows/windows.py#L428)

Computes the Hamming window.

The Hamming window is defined as follows:

wn=α−β cos⁡(2πnM−1)w_n = \alpha - \beta\ \cos \left( \frac{2 \pi n}{M - 1} \right)

wn​=α−β cos(M−12πn​)

The window is normalized to 1 (maximum value is 1). However, the 1 doesn't appear if `M` is even and `sym` is True.

Parameters:

**M** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the length of the window.
In other words, the number of points of the returned window.

Keyword Arguments:

- **sym** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If False, returns a periodic window suitable for use in spectral analysis.
If True, returns a symmetric window suitable for use in filter design. Default: True.
- **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - The coefficient α\alphaα in the equation above.
- **beta** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - The coefficient β\betaβ in the equation above.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](torch.set_default_dtype.html#torch.set_default_dtype)).
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). `device` will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Examples:

```
>>> # Generates a symmetric Hamming window.
>>> torch.signal.windows.hamming(10)
tensor([0.0800, 0.1876, 0.4601, 0.7700, 0.9723, 0.9723, 0.7700, 0.4601, 0.1876, 0.0800])

>>> # Generates a periodic Hamming window.
>>> torch.signal.windows.hamming(10, sym=False)
tensor([0.0800, 0.1679, 0.3979, 0.6821, 0.9121, 1.0000, 0.9121, 0.6821, 0.3979, 0.1679])
```