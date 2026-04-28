# torch.nn.utils.weight_norm

torch.nn.utils.weight_norm(*module*, *name='weight'*, *dim=0*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/nn/utils/weight_norm.py#L84)

Apply weight normalization to a parameter in the given module.

w=gv∥v∥\mathbf{w} = g \dfrac{\mathbf{v}}{\|\mathbf{v}\|}

w=g∥v∥v​

Weight normalization is a reparameterization that decouples the magnitude
of a weight tensor from its direction. This replaces the parameter specified
by `name` (e.g. `'weight'`) with two parameters: one specifying the magnitude
(e.g. `'weight_g'`) and one specifying the direction (e.g. `'weight_v'`).
Weight normalization is implemented via a hook that recomputes the weight
tensor from the magnitude and direction before every `forward()`
call.

By default, with `dim=0`, the norm is computed independently per output
channel/plane. To compute a norm over the entire weight tensor, use
`dim=None`.

See [https://arxiv.org/abs/1602.07868](https://arxiv.org/abs/1602.07868)

Warning

This function is deprecated. Use [`torch.nn.utils.parametrizations.weight_norm()`](torch.nn.utils.parametrizations.weight_norm.html#torch.nn.utils.parametrizations.weight_norm)
which uses the modern parametrization API. The new `weight_norm` is compatible
with `state_dict` generated from old `weight_norm`.

Migration guide:

- The magnitude (`weight_g`) and direction (`weight_v`) are now expressed
as `parametrizations.weight.original0` and `parametrizations.weight.original1`
respectively. If this is bothering you, please comment on
[pytorch/pytorch#102999](https://github.com/pytorch/pytorch/issues/102999)
- To remove the weight normalization reparameterization, use
[`torch.nn.utils.parametrize.remove_parametrizations()`](torch.nn.utils.parametrize.remove_parametrizations.html#torch.nn.utils.parametrize.remove_parametrizations).
- The weight is no longer recomputed once at module forward; instead, it will
be recomputed on every access. To restore the old behavior, use
[`torch.nn.utils.parametrize.cached()`](torch.nn.utils.parametrize.cached.html#torch.nn.utils.parametrize.cached) before invoking the module
in question.

Parameters:

- **module** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - containing module
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - name of weight parameter
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - dimension over which to compute the norm

Returns:

The original module with the weight norm hook

Return type:

*T_module*

Example:

```
>>> m = weight_norm(nn.Linear(20, 40), name='weight')
>>> m
Linear(in_features=20, out_features=40, bias=True)
>>> m.weight_g.size()
torch.Size([40, 1])
>>> m.weight_v.size()
torch.Size([40, 20])
```