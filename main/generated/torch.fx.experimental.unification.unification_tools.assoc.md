# torch.fx.experimental.unification.unification_tools.assoc

torch.fx.experimental.unification.unification_tools.assoc(*d*, *key*, *value*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/44a629b353df33cd84f67a031bba5b6313160a1c/torch/fx/experimental/unification/unification_tools.py#L225)

Return a new dict with new key value pair

New dict has d[key] set to value. Does not modify the initial dictionary.

```
>>> assoc({"x": 1}, "x", 2)
{'x': 2}
>>> assoc({"x": 1}, "y", 3) 
{'x': 1, 'y': 3}
```

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[*_K*, *_V*]