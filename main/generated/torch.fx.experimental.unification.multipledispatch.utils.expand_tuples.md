# torch.fx.experimental.unification.multipledispatch.utils.expand_tuples

torch.fx.experimental.unification.multipledispatch.utils.expand_tuples(*L*)[[source]](https://github.com/pytorch/pytorch/blob/12a9ea264bf805a66cd87e19e767ab23c2f59fef/torch/fx/experimental/unification/multipledispatch/utils.py#L27)

```
>>> expand_tuples([1, (2, 3)])
[(1, 2), (1, 3)]
>>> expand_tuples([1, 2])
[(1, 2)]
```

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type), ...]]