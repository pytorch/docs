# torch.compiler.is_exporting

torch.compiler.is_exporting()[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/compiler/__init__.py#L735)

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