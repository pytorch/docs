# torch.nn.utils.remove_weight_norm

torch.nn.utils.remove_weight_norm(*module*, *name='weight'*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/nn/utils/weight_norm.py#L148)

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