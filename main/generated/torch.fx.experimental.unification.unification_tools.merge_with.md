# torch.fx.experimental.unification.unification_tools.merge_with

torch.fx.experimental.unification.unification_tools.merge_with(*func*, **dicts*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/fx/experimental/unification/unification_tools.py#L70)

Merge dictionaries and apply function to combined values

A key may occur in more than one dict, and all values mapped from the key
will be passed to the function as a list, such as func([val1, val2, ...]).

```
>>> merge_with(sum, {1: 1, 2: 2}, {1: 10, 2: 20})
{1: 11, 2: 22}
```

```
>>> merge_with(first, {1: 1, 2: 2}, {2: 20, 3: 30}) 
{1: 1, 2: 2, 3: 30}
```

See also

merge

Return type:

[object](https://docs.python.org/3/builtins/functions.html#object)