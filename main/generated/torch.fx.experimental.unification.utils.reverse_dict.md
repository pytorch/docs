# torch.fx.experimental.unification.utils.reverse_dict

torch.fx.experimental.unification.utils.reverse_dict(*d*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/fx/experimental/unification/utils.py#L84)

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

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[_T, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[_T, ...]]