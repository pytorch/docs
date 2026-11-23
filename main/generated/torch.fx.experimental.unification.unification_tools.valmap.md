# torch.fx.experimental.unification.unification_tools.valmap

torch.fx.experimental.unification.unification_tools.valmap(*func*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/e9565720ab4f59a0ed491b3f8440ae38c2455bab/torch/fx/experimental/unification/unification_tools.py#L101)

Apply function to values of dictionary

```
>>> bills = {"Alice": [20, 15, 30], "Bob": [10, 35]}
>>> valmap(sum, bills) 
{'Alice': 65, 'Bob': 45}
```

See also

keymap
itemmap

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[_K, _V2]