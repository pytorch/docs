# torch.fx.experimental.unification.unification_tools.valfilter

torch.fx.experimental.unification.unification_tools.valfilter(*predicate*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/fx/experimental/unification/unification_tools.py#L155)

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

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[_K, _V]