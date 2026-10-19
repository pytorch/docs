# torch.compiler.is_exporting

torch.compiler.is_exporting()[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/compiler/__init__.py#L736)

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