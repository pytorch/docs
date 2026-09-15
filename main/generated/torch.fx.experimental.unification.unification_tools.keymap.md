# torch.fx.experimental.unification.unification_tools.keymap

torch.fx.experimental.unification.unification_tools.keymap(*func*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/fx/experimental/unification/unification_tools.py#L119)

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

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[_K2, _V]