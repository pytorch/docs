# torch.nn.utils.prune.l1_unstructured

torch.nn.utils.prune.l1_unstructured(*module*, *name*, *amount*, *importance_scores=None*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/nn/utils/prune.py#L908)

Prune tensor by removing units with the lowest L1-norm.

Prunes tensor corresponding to parameter called `name` in `module`
by removing the specified amount of (currently unpruned) units with the
lowest L1-norm.
Modifies module in place (and also return the modified module)
by:

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
- **importance_scores** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - tensor of importance scores (of same
shape as module parameter) used to compute mask for pruning.
The values in this tensor indicate the importance of the corresponding
elements in the parameter being pruned.
If unspecified or None, the module parameter will be used in its place.

Returns:

modified (i.e. pruned) version of the input module

Return type:

module ([nn.Module](torch.nn.Module.html#torch.nn.Module))

Examples

```
>>> m = prune.l1_unstructured(nn.Linear(2, 3), "weight", amount=0.2)
>>> m.state_dict().keys()
odict_keys(['bias', 'weight_orig', 'weight_mask'])
```