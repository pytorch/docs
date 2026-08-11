# torch.isclose

torch.isclose(*input*, *other*, *rtol=1e-05*, *atol=1e-08*, *equal_nan=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with boolean elements representing if each element of
`input` is "close" to the corresponding element of `other`.
Closeness is defined as:

∣inputi−otheri∣≤rtol×∣otheri∣+atol\lvert \text{input}_i - \text{other}_i \rvert \leq \texttt{rtol} \times \lvert \text{other}_i \rvert + \texttt{atol}

∣inputi​−otheri​∣≤rtol×∣otheri​∣+atol

where `input` and `other` are finite. Where `input`
and/or `other` are nonfinite they are close if and only if
they are equal, with NaNs being considered equal to each other when
`equal_nan` is True.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - first tensor to compare
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - second tensor to compare
- **rtol** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - relative tolerance. Default: 1e-05
- **atol** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - absolute tolerance. Default: 1e-08
- **equal_nan** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True`, then two `NaN` s will be considered equal. Default: `False`

Examples:

```
>>> torch.isclose(torch.tensor((1., 2, 3)), torch.tensor((1 + 1e-10, 3, 4)))
tensor([ True, False, False])
>>> torch.isclose(torch.tensor((float('inf'), 4)), torch.tensor((float('inf'), 6)), rtol=.5)
tensor([True, True])
```