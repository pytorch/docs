# torch.fx.experimental.unification.unification_tools.itemmap

torch.fx.experimental.unification.unification_tools.itemmap(*func*, *d*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/fx/experimental/unification/unification_tools.py#L137)

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

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[object](https://docs.python.org/3/builtins/functions.html#object), [object](https://docs.python.org/3/builtins/functions.html#object)]