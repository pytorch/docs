# torch.fx.experimental.unification.unification_tools.merge

torch.fx.experimental.unification.unification_tools.merge(**dicts*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/fx/experimental/unification/unification_tools.py#L46)

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

[object](https://docs.python.org/3/library/functions.html#object)