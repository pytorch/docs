# torch.fx.experimental.unification.unification_tools.merge

torch.fx.experimental.unification.unification_tools.merge(**dicts*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/08c2d21eeac45d7bb2b95f497938e99c0250222d/torch/fx/experimental/unification/unification_tools.py#L46)

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