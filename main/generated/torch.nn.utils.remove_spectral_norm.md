# torch.nn.utils.remove_spectral_norm

torch.nn.utils.remove_spectral_norm(*module*, *name='weight'*)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/nn/utils/spectral_norm.py#L335)

Remove the spectral normalization reparameterization from a module.

Parameters:

- **module** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - containing module
- **name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**optional*) - name of weight parameter

Return type:

*T_module*

Example

```
>>> m = spectral_norm(nn.Linear(40, 10))
>>> remove_spectral_norm(m)
```