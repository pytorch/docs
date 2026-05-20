# torch.fx.experimental.unification.unification_tools.itemfilter

torch.fx.experimental.unification.unification_tools.itemfilter(*predicate*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/fx/experimental/unification/unification_tools.py#L199)

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

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[_K, _V]