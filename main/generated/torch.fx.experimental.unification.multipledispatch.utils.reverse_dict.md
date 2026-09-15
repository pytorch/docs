# torch.fx.experimental.unification.multipledispatch.utils.reverse_dict

torch.fx.experimental.unification.multipledispatch.utils.reverse_dict(*d*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/fx/experimental/unification/multipledispatch/utils.py#L78)

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
as undeterministic.

Return type:

OrderedDict[_T, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[_T, ...]]