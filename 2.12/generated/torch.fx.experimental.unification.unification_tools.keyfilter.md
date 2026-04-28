# torch.fx.experimental.unification.unification_tools.keyfilter

torch.fx.experimental.unification.unification_tools.keyfilter(*predicate*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/fx/experimental/unification/unification_tools.py#L155)

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