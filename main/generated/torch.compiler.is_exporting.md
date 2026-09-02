# torch.compiler.is_exporting

torch.compiler.is_exporting()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/compiler/__init__.py#L735)

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

[bool](https://docs.python.org/3/library/functions.html#bool)