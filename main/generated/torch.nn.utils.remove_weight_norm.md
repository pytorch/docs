# torch.nn.utils.remove_weight_norm

torch.nn.utils.remove_weight_norm(*module*, *name='weight'*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/nn/utils/weight_norm.py#L148)

Remove the weight normalization reparameterization from a module.

Parameters:

- **module** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - containing module
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - name of weight parameter

Return type:

*T_module*

Example

```
>>> m = weight_norm(nn.Linear(20, 40))
>>> remove_weight_norm(m)
```