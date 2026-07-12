# torch.fx.experimental.unification.utils.reverse_dict

torch.fx.experimental.unification.utils.reverse_dict(*d*)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/fx/experimental/unification/utils.py#L84)

Reverses direction of dependence dict.

```
>>> d = {"a": (1, 2), "b": (2, 3), "c": ()}
>>> reverse_dict(d) 
{1: ('a',), 2: ('a', 'b'), 3: ('b',)}
```

Note

dict order are not deterministic. As we iterate on the
input dict, it make the output of this function depend on the
dict order. So this function output order should be considered
as undeterministic.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[_T, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[_T, ...]]