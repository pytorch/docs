# torch.nn.utils.prune.random_unstructured

torch.nn.utils.prune.random_unstructured(*module*, *name*, *amount*)[[source]](https://github.com/pytorch/pytorch/blob/40e21dcd4b92d59842b3e3b7f542f855dedddb91/torch/nn/utils/prune.py#L871)

Prune tensor by removing random (currently unpruned) units.

Prunes tensor corresponding to parameter called `name` in `module`
by removing the specified `amount` of (currently unpruned) units
selected at random.
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
- **amount** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*float*](https://docs.python.org/3/library/functions.html#float)) - quantity of parameters to prune.
If `float`, should be between 0.0 and 1.0 and represent the
fraction of parameters to prune. If `int`, it represents the
absolute number of parameters to prune.

Returns:

modified (i.e. pruned) version of the input module

Return type:

module ([nn.Module](torch.nn.Module.html#torch.nn.Module))

Examples

```
>>> m = prune.random_unstructured(nn.Linear(2, 3), "weight", amount=1)
>>> torch.sum(m.weight_mask == 0)
tensor(1)
```