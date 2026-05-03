# torch.fx.experimental.unification.unification_tools.keymap

torch.fx.experimental.unification.unification_tools.keymap(*func*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/fx/experimental/unification/unification_tools.py#L119)

Apply function to keys of dictionary

```
>>> bills = {"Alice": [20, 15, 30], "Bob": [10, 35]}
>>> keymap(str.lower, bills) 
{'alice': [20, 15, 30], 'bob': [10, 35]}
```

See also

valmap
itemmap

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[_K2, _V]