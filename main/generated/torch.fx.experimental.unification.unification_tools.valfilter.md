# torch.fx.experimental.unification.unification_tools.valfilter

torch.fx.experimental.unification.unification_tools.valfilter(*predicate*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/fx/experimental/unification/unification_tools.py#L155)

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