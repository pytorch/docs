# torch.signal.windows.windows.bartlett

torch.signal.windows.windows.bartlett(*M*, ***, *sym=True*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*)[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/signal/windows/windows.py#L597)

Computes the Bartlett window.

The Bartlett window is defined as follows:

wn=1−∣2nM−1−1∣={2nM−1if 0≤n≤M−122−2nM−1if M−12<n<Mw_n = 1 - \left| \frac{2n}{M - 1} - 1 \right| = \begin{cases}
 \frac{2n}{M - 1} & \text{if } 0 \leq n \leq \frac{M - 1}{2} \\
 2 - \frac{2n}{M - 1} & \text{if } \frac{M - 1}{2} < n < M \\ \end{cases}

wn​=1−​M−12n​−1​={M−12n​2−M−12n​​if 0≤n≤2M−1​if 2M−1​<n<M​

The window is normalized to 1 (maximum value is 1). However, the 1 doesn't appear if `M` is even and `sym` is True.

Parameters:

**M** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the length of the window.
In other words, the number of points of the returned window.

Keyword Arguments:

- **sym** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If False, returns a periodic window suitable for use in spectral analysis.
If True, returns a symmetric window suitable for use in filter design. Default: True.
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
>>> # Generates a symmetric Bartlett window.
>>> torch.signal.windows.bartlett(10)
tensor([0.0000, 0.2222, 0.4444, 0.6667, 0.8889, 0.8889, 0.6667, 0.4444, 0.2222, 0.0000])

>>> # Generates a periodic Bartlett window.
>>> torch.signal.windows.bartlett(10, sym=False)
tensor([0.0000, 0.2000, 0.4000, 0.6000, 0.8000, 1.0000, 0.8000, 0.6000, 0.4000, 0.2000])
```