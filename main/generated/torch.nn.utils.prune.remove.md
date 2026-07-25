# torch.nn.utils.prune.remove

torch.nn.utils.prune.remove(*module*, *name*)[[source]](https://github.com/pytorch/pytorch/blob/55d182046edce7face6d9eb894f23b3a2588d876/torch/nn/utils/prune.py#L1197)

Remove the pruning reparameterization from a module and the pruning method from the forward hook.

The pruned parameter named `name` remains permanently pruned, and the parameter
named `name+'_orig'` is removed from the parameter list. Similarly,
the buffer named `name+'_mask'` is removed from the buffers.

Note

Pruning itself is NOT undone or reversed!

Parameters:

- **module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module containing the tensor to prune
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - parameter name within `module` on which pruning
will act.

Examples

```
>>> m = random_unstructured(nn.Linear(5, 7), name="weight", amount=0.2)
>>> m = remove(m, name="weight")
```