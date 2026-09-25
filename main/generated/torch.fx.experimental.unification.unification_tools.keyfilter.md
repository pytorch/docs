# torch.fx.experimental.unification.unification_tools.keyfilter

torch.fx.experimental.unification.unification_tools.keyfilter(*predicate*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/fx/experimental/unification/unification_tools.py#L177)

Filter items in dictionary by key

```
>>> iseven = lambda x: x % 2 == 0
>>> d = {1: 2, 2: 3, 3: 4, 4: 5}
>>> keyfilter(iseven, d)
{2: 3, 4: 5}
```

See also

valfilter
itemfilter
keymap

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[_K, _V]