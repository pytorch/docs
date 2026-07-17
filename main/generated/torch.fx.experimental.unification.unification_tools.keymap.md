# torch.fx.experimental.unification.unification_tools.keymap

torch.fx.experimental.unification.unification_tools.keymap(*func*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/3fadfe4be9707a8a43a23db6e0da32dc1b507694/torch/fx/experimental/unification/unification_tools.py#L119)

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