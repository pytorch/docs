# torch.allclose

torch.allclose(*input: [Tensor](../tensors.html#torch.Tensor)*, *other: [Tensor](../tensors.html#torch.Tensor)*, *rtol: [float](https://docs.python.org/3/library/functions.html#float) = 1e-05*, *atol: [float](https://docs.python.org/3/library/functions.html#float) = 1e-08*, *equal_nan: [bool](https://docs.python.org/3/library/functions.html#bool) = False*) → [bool](https://docs.python.org/3/library/functions.html#bool)

This function checks if `input` and `other` satisfy the condition:

∣inputi−otheri∣≤atol+rtol×∣otheri∣\lvert \text{input}_i - \text{other}_i \rvert \leq \texttt{atol} + \texttt{rtol} \times \lvert \text{other}_i \rvert

∣inputi​−otheri​∣≤atol+rtol×∣otheri​∣

elementwise, for all elements of `input` and `other`. The behaviour of this function is analogous to
[numpy.allclose](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html)

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - first tensor to compare
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - second tensor to compare
- **atol** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - absolute tolerance. Default: 1e-08
- **rtol** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - relative tolerance. Default: 1e-05
- **equal_nan** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True`, then two `NaN` s will be considered equal. Default: `False`

Example:

```
>>> torch.allclose(torch.tensor([10000., 1e-07]), torch.tensor([10000.1, 1e-08]))
False
>>> torch.allclose(torch.tensor([10000., 1e-08]), torch.tensor([10000.1, 1e-09]))
True
>>> torch.allclose(torch.tensor([1.0, float('nan')]), torch.tensor([1.0, float('nan')]))
False
>>> torch.allclose(torch.tensor([1.0, float('nan')]), torch.tensor([1.0, float('nan')]), equal_nan=True)
True
```