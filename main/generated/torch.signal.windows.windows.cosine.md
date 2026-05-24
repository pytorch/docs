# torch.signal.windows.windows.cosine

torch.signal.windows.windows.cosine(*M*, ***, *sym=True*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*)[[source]](https://github.com/pytorch/pytorch/blob/15e96b281415c58d3acf5d63d86df9d68744ee16/torch/signal/windows/windows.py#L178)

Computes a window with a simple cosine waveform, following the same implementation as SciPy.
This window is also known as the sine window.

The cosine window is defined as follows:

wn=sin⁡(π(n+0.5)M)w_n = \sin\left(\frac{\pi (n + 0.5)}{M}\right)

wn​=sin(Mπ(n+0.5)​)

This formula differs from the typical cosine window formula by incorporating a 0.5 term in the numerator,
which shifts the sample positions. This adjustment results in a window that starts and ends with non-zero values.

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
>>> # Generates a symmetric cosine window.
>>> torch.signal.windows.cosine(10)
tensor([0.1564, 0.4540, 0.7071, 0.8910, 0.9877, 0.9877, 0.8910, 0.7071, 0.4540, 0.1564])

>>> # Generates a periodic cosine window.
>>> torch.signal.windows.cosine(10, sym=False)
tensor([0.1423, 0.4154, 0.6549, 0.8413, 0.9595, 1.0000, 0.9595, 0.8413, 0.6549, 0.4154])
```