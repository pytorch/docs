# torch.fx.experimental.unification.unification_tools.itemmap

torch.fx.experimental.unification.unification_tools.itemmap(*func*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/fx/experimental/unification/unification_tools.py#L137)

Apply function to items of dictionary

```
>>> accountids = {"Alice": 10, "Bob": 20}
>>> itemmap(reversed, accountids) 
{10: "Alice", 20: "Bob"}
```

See also

keymap
valmap

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[object](https://docs.python.org/3/library/functions.html#object), [object](https://docs.python.org/3/library/functions.html#object)]