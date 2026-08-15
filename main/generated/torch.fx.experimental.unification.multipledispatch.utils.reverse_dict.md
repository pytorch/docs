# torch.fx.experimental.unification.multipledispatch.utils.reverse_dict

torch.fx.experimental.unification.multipledispatch.utils.reverse_dict(*d*)[[source]](https://github.com/pytorch/pytorch/blob/55dfacc69b3a9156f68cfe07b61553e4bdc7de29/torch/fx/experimental/unification/multipledispatch/utils.py#L78)

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

OrderedDict[_T, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[_T, ...]]