# torch.nn.utils.prune.is_pruned

torch.nn.utils.prune.is_pruned(*module*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/nn/utils/prune.py#L1227)

Check if a module is pruned by looking for pruning pre-hooks.

Check whether `module` is pruned by looking for
`forward_pre_hooks` in its modules that inherit from the
[`BasePruningMethod`](torch.nn.utils.prune.BasePruningMethod.html#torch.nn.utils.prune.BasePruningMethod).

Parameters:

**module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - object that is either pruned or unpruned

Returns:

binary answer to whether `module` is pruned.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

Examples

```
>>> from torch.nn.utils import prune
>>> m = nn.Linear(5, 7)
>>> print(prune.is_pruned(m))
False
>>> prune.random_unstructured(m, name="weight", amount=0.2)
>>> print(prune.is_pruned(m))
True
```