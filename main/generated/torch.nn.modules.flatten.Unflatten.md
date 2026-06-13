# Unflatten

*class*torch.nn.modules.flatten.Unflatten(*dim*, *unflattened_size*)[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/nn/modules/flatten.py#L64)

Unflattens a tensor dim expanding it to a desired shape. For use with `Sequential`.

- `dim` specifies the dimension of the input tensor to be unflattened.
- `unflattened_size` is the new shape of the unflattened dimension of the tensor and it can be
a tuple of ints or a list of ints or torch.Size for Tensor input.

Shape:

- Input: (∗,Sdim,∗)(*, S_{\text{dim}}, *)(∗,Sdim​,∗), where SdimS_{\text{dim}}Sdim​ is the size at
dimension `dim` and ∗*∗ means any number of dimensions including none.
- Output: (∗,U1,...,Un,∗)(*, U_1, ..., U_n, *)(∗,U1​,...,Un​,∗), where UUU = `unflattened_size` and
∏i=1nUi=Sdim\prod_{i=1}^n U_i = S_{\text{dim}}∏i=1n​Ui​=Sdim​.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Dimension to be unflattened
- **unflattened_size** (*Union**[*[*torch.Size*](../size.html#torch.Size)*,**Tuple**,**List**]*) - New shape of the unflattened dimension

Examples

```
>>> input = torch.randn(2, 50)
>>> # With tuple of ints
>>> m = nn.Sequential(
>>> nn.Linear(50, 50),
>>> nn.Unflatten(1, (2, 5, 5))
>>> )
>>> output = m(input)
>>> output.size()
torch.Size([2, 2, 5, 5])
>>> # With torch.Size
>>> m = nn.Sequential(
>>> nn.Linear(50, 50),
>>> nn.Unflatten(1, torch.Size([2, 5, 5]))
>>> )
>>> output = m(input)
>>> output.size()
torch.Size([2, 2, 5, 5])
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/nn/modules/flatten.py#L132)

Returns the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/nn/modules/flatten.py#L126)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)