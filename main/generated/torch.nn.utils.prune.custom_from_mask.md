# torch.nn.utils.prune.custom_from_mask

torch.nn.utils.prune.custom_from_mask(*module*, *name*, *mask*)[[source]](https://github.com/pytorch/pytorch/blob/13818df097cc56c9a2a860678049f2a42a008853/torch/nn/utils/prune.py#L1164)

Prune tensor corresponding to parameter called `name` in `module` by applying the pre-computed mask in `mask`.

Modifies module in place (and also return the modified module) by:

1. adding a named buffer called `name+'_mask'` corresponding to the
binary mask applied to the parameter `name` by the pruning method.
2. replacing the parameter `name` by its pruned version, while the
original (unpruned) parameter is stored in a new parameter named
`name+'_orig'`.

Parameters:

- **module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module containing the tensor to prune
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - parameter name within `module` on which pruning
will act.
- **mask** ([*Tensor*](../tensors.html#torch.Tensor)) - binary mask to be applied to the parameter.

Returns:

modified (i.e. pruned) version of the input module

Return type:

module ([nn.Module](torch.nn.Module.html#torch.nn.Module))

Examples

```
>>> from torch.nn.utils import prune
>>> m = prune.custom_from_mask(
... nn.Linear(5, 3), name="bias", mask=torch.tensor([0, 1, 0])
... )
>>> print(m.bias_mask)
tensor([0., 1., 0.])
```