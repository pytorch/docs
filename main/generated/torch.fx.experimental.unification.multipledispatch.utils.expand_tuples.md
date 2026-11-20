# torch.fx.experimental.unification.multipledispatch.utils.expand_tuples

torch.fx.experimental.unification.multipledispatch.utils.expand_tuples(*L*)[[source]](https://github.com/pytorch/pytorch/blob/efbc87071fdf61bd50d5dc3b315b65bd452c401d/torch/fx/experimental/unification/multipledispatch/utils.py#L27)

```
>>> expand_tuples([1, (2, 3)])
[(1, 2), (1, 3)]
>>> expand_tuples([1, 2])
[(1, 2)]
```

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[type](https://docs.python.org/3/builtins/functions.html#type), ...]]