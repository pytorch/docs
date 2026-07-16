# torch.nn.utils.prune.ln_structured

torch.nn.utils.prune.ln_structured(*module*, *name*, *amount*, *n*, *dim*, *importance_scores=None*)[[source]](https://github.com/pytorch/pytorch/blob/a37249c7e9824d557710fe7682d943593ef355d8/torch/nn/utils/prune.py#L991)

Prune tensor by removing channels with the lowest L`n`-norm along the specified dimension.

Prunes tensor corresponding to parameter called `name` in `module`
by removing the specified `amount` of (currently unpruned) channels
along the specified `dim` with the lowest L`n`-norm.
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
- **n** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*float*](https://docs.python.org/3/library/functions.html#float)*,**inf**,**-inf**,**'fro'**,**'nuc'*) - See documentation of valid
entries for argument `p` in [`torch.norm()`](torch.norm.html#torch.norm).
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - index of the dim along which we define channels to prune.
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
>>> from torch.nn.utils import prune
>>> m = prune.ln_structured(
... nn.Conv2d(5, 3, 2), "weight", amount=0.3, dim=1, n=float("-inf")
... )
```