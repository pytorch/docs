# torch.fx.experimental.unification.unification_tools.assoc

torch.fx.experimental.unification.unification_tools.assoc(*d*, *key*, *value*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/fx/experimental/unification/unification_tools.py#L199)

Return a new dict with new key value pair

New dict has d[key] set to value. Does not modify the initial dictionary.

```
>>> assoc({"x": 1}, "x", 2)
{'x': 2}
>>> assoc({"x": 1}, "y", 3) 
{'x': 1, 'y': 3}
```