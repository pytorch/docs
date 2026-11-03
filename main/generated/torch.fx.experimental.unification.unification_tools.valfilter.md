# torch.fx.experimental.unification.unification_tools.valfilter

torch.fx.experimental.unification.unification_tools.valfilter(*predicate*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/fbab7cc90f5699714d5785aaa2f153c739435d6f/torch/fx/experimental/unification/unification_tools.py#L155)

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