# torch.fx.experimental.unification.unification_tools.merge

torch.fx.experimental.unification.unification_tools.merge(**dicts*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/fx/experimental/unification/unification_tools.py#L46)

Merge a collection of dictionaries

```
>>> merge({1: "one"}, {2: "two"})
{1: 'one', 2: 'two'}
```

Later dictionaries have precedence

```
>>> merge({1: 2, 3: 4}, {3: 3, 4: 4})
{1: 2, 3: 3, 4: 4}
```

See also

merge_with

Return type:

[object](https://docs.python.org/3/builtins/functions.html#object)