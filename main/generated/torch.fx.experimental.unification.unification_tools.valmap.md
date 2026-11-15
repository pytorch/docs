# torch.fx.experimental.unification.unification_tools.valmap

torch.fx.experimental.unification.unification_tools.valmap(*func*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/c79633996ebc2114482ae5a4ff3cb409d79a8a9c/torch/fx/experimental/unification/unification_tools.py#L101)

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