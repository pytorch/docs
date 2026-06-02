# torch.fx.experimental.unification.unification_tools.keymap

torch.fx.experimental.unification.unification_tools.keymap(*func*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/fx/experimental/unification/unification_tools.py#L119)

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