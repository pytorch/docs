# torch.compiler.is_exporting

torch.compiler.is_exporting()[[source]](https://github.com/pytorch/pytorch/blob/e1994aea9ce307fb82feeb7524ab2c5d36771e4f/torch/compiler/__init__.py#L739)

Indicates whether we're under exporting.

It's stricter than is_compiling() flag, as it would only be set to True when
torch.export is used.

Example:

```
>>> def forward(self, x):
>>> if not torch.compiler.is_exporting():
>>> pass # ...logic that is not needed in export...
>>>
>>> # ...rest of the function...
```

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)