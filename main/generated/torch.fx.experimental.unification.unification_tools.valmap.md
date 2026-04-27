# torch.fx.experimental.unification.unification_tools.valmap

torch.fx.experimental.unification.unification_tools.valmap(*func*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/fx/experimental/unification/unification_tools.py#L101)

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

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[_K, _V2]