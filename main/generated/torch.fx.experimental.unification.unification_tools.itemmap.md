# torch.fx.experimental.unification.unification_tools.itemmap

torch.fx.experimental.unification.unification_tools.itemmap(*func*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/fx/experimental/unification/unification_tools.py#L137)

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