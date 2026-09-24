# torch.fx.experimental.unification.utils.reverse_dict

torch.fx.experimental.unification.utils.reverse_dict(*d*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/fx/experimental/unification/utils.py#L84)

Reverses direction of dependence dict.

```
>>> d = {"a": (1, 2), "b": (2, 3), "c": ()}
>>> reverse_dict(d) 
{1: ('a',), 2: ('a', 'b'), 3: ('b',)}
```

Note

dict order is not deterministic. As we iterate on the
input dict, it makes the output of this function depend on the
dict order. So this function output order should be considered
as nondeterministic.

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[_T, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[_T, ...]]