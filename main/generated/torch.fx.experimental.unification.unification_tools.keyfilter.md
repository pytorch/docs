# torch.fx.experimental.unification.unification_tools.keyfilter

torch.fx.experimental.unification.unification_tools.keyfilter(*predicate*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/fx/experimental/unification/unification_tools.py#L177)

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

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[_K, _V]