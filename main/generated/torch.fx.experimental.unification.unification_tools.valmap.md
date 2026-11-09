# torch.fx.experimental.unification.unification_tools.valmap

torch.fx.experimental.unification.unification_tools.valmap(*func*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/50d50e722913b05a0762c886507c9be7ae43d2f3/torch/fx/experimental/unification/unification_tools.py#L101)

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