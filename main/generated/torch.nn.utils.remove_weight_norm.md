# torch.nn.utils.remove_weight_norm

torch.nn.utils.remove_weight_norm(*module*, *name='weight'*)[[source]](https://github.com/pytorch/pytorch/blob/3af07571b9d7402fd74352d079e6ff5fa307ec5f/torch/nn/utils/weight_norm.py#L149)

Remove the weight normalization reparameterization from a module.

Parameters:

- **module** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - containing module
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - name of weight parameter

Return type:

*T_module*

Example

```
>>> warnings.filterwarnings(
... "ignore", message=".*torch.nn.utils.weight_norm"
... ) # docs: hide
>>> m = weight_norm(nn.Linear(20, 40))
>>> remove_weight_norm(m)
```