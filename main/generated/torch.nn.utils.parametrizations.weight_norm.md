# torch.nn.utils.parametrizations.weight_norm

torch.nn.utils.parametrizations.weight_norm(*module*, *name='weight'*, *dim=0*)[[source]](https://github.com/pytorch/pytorch/blob/c9fded8194d3b089ed610b586eb746a6e74c6616/torch/nn/utils/parametrizations.py#L336)

Apply weight normalization to a parameter in the given module.

w=gv∥v∥\mathbf{w} = g \dfrac{\mathbf{v}}{\|\mathbf{v}\|}

w=g∥v∥v​

Weight normalization is a reparameterization that decouples the magnitude
of a weight tensor from its direction. This replaces the parameter specified
by `name` with two parameters: one specifying the magnitude
and one specifying the direction.

By default, with `dim=0`, the norm is computed independently per output
channel/plane. To compute a norm over the entire weight tensor, use
`dim=None`.

See [https://arxiv.org/abs/1602.07868](https://arxiv.org/abs/1602.07868)

Parameters:

- **module** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - containing module
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - name of weight parameter
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - dimension over which to compute the norm

Returns:

The original module with the weight norm hook

Example:

```
>>> m = weight_norm(nn.Linear(20, 40), name='weight')
>>> m
ParametrizedLinear(
 in_features=20, out_features=40, bias=True
 (parametrizations): ModuleDict(
 (weight): ParametrizationList(
 (0): _WeightNorm()
 )
 )
)
>>> m.parametrizations.weight.original0.size()
torch.Size([40, 1])
>>> m.parametrizations.weight.original1.size()
torch.Size([40, 20])
```