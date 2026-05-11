# torch.nn.utils.remove_spectral_norm

torch.nn.utils.remove_spectral_norm(*module*, *name='weight'*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/nn/utils/spectral_norm.py#L335)

Remove the spectral normalization reparameterization from a module.

Parameters:

- **module** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - containing module
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - name of weight parameter

Return type:

*T_module*

Example

```
>>> m = spectral_norm(nn.Linear(40, 10))
>>> remove_spectral_norm(m)
```