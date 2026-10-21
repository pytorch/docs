# torch.fx.experimental.unification.unification_tools.itemfilter

torch.fx.experimental.unification.unification_tools.itemfilter(*predicate*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/7ffd47d270087d6dbafb876c0549d949aabf0a5a/torch/fx/experimental/unification/unification_tools.py#L199)

Filter items in dictionary by item

```
>>> def isvalid(item):
... k, v = item
... return k % 2 == 0 and v < 4
```

```
>>> d = {1: 2, 2: 3, 3: 4, 4: 5}
>>> itemfilter(isvalid, d)
{2: 3}
```

See also

keyfilter
valfilter
itemmap

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[_K, _V]