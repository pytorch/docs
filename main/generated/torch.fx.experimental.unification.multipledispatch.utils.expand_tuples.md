# torch.fx.experimental.unification.multipledispatch.utils.expand_tuples

torch.fx.experimental.unification.multipledispatch.utils.expand_tuples(*L*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/fx/experimental/unification/multipledispatch/utils.py#L27)

```
>>> expand_tuples([1, (2, 3)])
[(1, 2), (1, 3)]
>>> expand_tuples([1, 2])
[(1, 2)]
```

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type), ...]]