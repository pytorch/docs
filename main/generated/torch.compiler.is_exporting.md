# torch.compiler.is_exporting

torch.compiler.is_exporting()[[source]](https://github.com/pytorch/pytorch/blob/fe3f518c806b6f1fb8acc283135e5414b8606887/torch/compiler/__init__.py#L735)

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