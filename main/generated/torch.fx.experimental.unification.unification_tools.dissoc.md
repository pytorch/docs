# torch.fx.experimental.unification.unification_tools.dissoc

torch.fx.experimental.unification.unification_tools.dissoc(*d*, **keys*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/b8bd7cf750ea02a2390d8a5440261e2c6ed5ddc7/torch/fx/experimental/unification/unification_tools.py#L243)

Return a new dict with the given key(s) removed.

New dict has d[key] deleted for each supplied key.
Does not modify the initial dictionary.

```
>>> dissoc({"x": 1, "y": 2}, "y")
{'x': 1}
>>> dissoc({"x": 1, "y": 2}, "y", "x")
{}
>>> dissoc({"x": 1}, "y") # Ignores missing keys
{'x': 1}
```

Return type:

[object](https://docs.python.org/3/builtins/functions.html#object)