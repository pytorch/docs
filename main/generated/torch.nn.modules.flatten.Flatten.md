# Flatten

*class*torch.nn.modules.flatten.Flatten(*start_dim=1*, *end_dim=-1*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/nn/modules/flatten.py#L12)

Flattens a contiguous range of dims into a tensor.

For use with `Sequential`, see [`torch.flatten()`](torch.flatten.html#torch.flatten) for details.

Shape:

- Input: (∗,Sstart,...,Si,...,Send,∗)(*, S_{\text{start}},..., S_{i}, ..., S_{\text{end}}, *)(∗,Sstart​,...,Si​,...,Send​,∗),'
where SiS_{i}Si​ is the size at dimension iii and ∗*∗ means any
number of dimensions including none.
- Output: (∗,∏i=startendSi,∗)(*, \prod_{i=\text{start}}^{\text{end}} S_{i}, *)(∗,∏i=startend​Si​,∗).

Parameters:

- **start_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - first dim to flatten (default = 1).
- **end_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - last dim to flatten (default = -1).

Examples::

```
>>> input = torch.randn(32, 1, 5, 5)
>>> # With default parameters
>>> m = nn.Flatten()
>>> output = m(input)
>>> output.size()
torch.Size([32, 25])
>>> # With non-default parameters
>>> m = nn.Flatten(0, 2)
>>> output = m(input)
>>> output.size()
torch.Size([160, 5])
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/nn/modules/flatten.py#L57)

Returns the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/nn/modules/flatten.py#L51)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)