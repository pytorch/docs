# torch.fx.experimental.unification.unification_tools.valfilter

torch.fx.experimental.unification.unification_tools.valfilter(*predicate*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/fx/experimental/unification/unification_tools.py#L155)

Filter items in dictionary by value

```
>>> iseven = lambda x: x % 2 == 0
>>> d = {1: 2, 2: 3, 3: 4, 4: 5}
>>> valfilter(iseven, d)
{1: 2, 3: 4}
```

See also

keyfilter
itemfilter
valmap

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[_K, _V]