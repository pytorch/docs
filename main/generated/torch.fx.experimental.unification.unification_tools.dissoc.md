# torch.fx.experimental.unification.unification_tools.dissoc

torch.fx.experimental.unification.unification_tools.dissoc(*d*, **keys*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/fx/experimental/unification/unification_tools.py#L243)

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

[object](https://docs.python.org/3/library/functions.html#object)