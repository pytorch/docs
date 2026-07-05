# torch.fx.experimental.unification.multipledispatch.utils.expand_tuples

torch.fx.experimental.unification.multipledispatch.utils.expand_tuples(*L*)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/fx/experimental/unification/multipledispatch/utils.py#L27)

```
>>> expand_tuples([1, (2, 3)])
[(1, 2), (1, 3)]
>>> expand_tuples([1, 2])
[(1, 2)]
```

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type), ...]]