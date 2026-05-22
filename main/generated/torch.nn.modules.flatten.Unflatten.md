# Unflatten

*class*torch.nn.modules.flatten.Unflatten(*dim*, *unflattened_size*)[[source]](https://github.com/pytorch/pytorch/blob/54541f51bee1b9b66a0ecb11e69067a677a60487/torch/nn/modules/flatten.py#L64)

Unflattens a tensor dim expanding it to a desired shape. For use with `Sequential`.

- `dim` specifies the dimension of the input tensor to be unflattened, and it can
be either int or str when Tensor or NamedTensor is used, respectively.
- `unflattened_size` is the new shape of the unflattened dimension of the tensor and it can be
a tuple of ints or a list of ints or torch.Size for Tensor input; a NamedShape
(tuple of (name, size) tuples) for NamedTensor input.

Shape:

- Input: (∗,Sdim,∗)(*, S_{\text{dim}}, *)(∗,Sdim​,∗), where SdimS_{\text{dim}}Sdim​ is the size at
dimension `dim` and ∗*∗ means any number of dimensions including none.
- Output: (∗,U1,...,Un,∗)(*, U_1, ..., U_n, *)(∗,U1​,...,Un​,∗), where UUU = `unflattened_size` and
∏i=1nUi=Sdim\prod_{i=1}^n U_i = S_{\text{dim}}∏i=1n​Ui​=Sdim​.

Parameters:

- **dim** (*Union**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) - Dimension to be unflattened
- **unflattened_size** (*Union**[*[*torch.Size*](../size.html#torch.Size)*,**Tuple**,**List**,**NamedShape**]*) - New shape of the unflattened dimension

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
>>> # With namedshape (tuple of tuples)
>>> input = torch.randn(2, 50, names=("N", "features"))
>>> unflatten = nn.Unflatten("features", (("C", 2), ("H", 5), ("W", 5)))
>>> output = unflatten(input)
>>> output.size()
torch.Size([2, 2, 5, 5])
```

NamedShape

alias of [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)[[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`int`](https://docs.python.org/3/library/functions.html#int)]]

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/54541f51bee1b9b66a0ecb11e69067a677a60487/torch/nn/modules/flatten.py#L163)

Returns the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/54541f51bee1b9b66a0ecb11e69067a677a60487/torch/nn/modules/flatten.py#L157)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)