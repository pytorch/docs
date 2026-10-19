# torch.compiler.is_compiling

torch.compiler.is_compiling()[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/compiler/__init__.py#L583)

Indicates whether a graph is executed/traced as part of torch.compile() or torch.export().

Note that there are 2 other related flags that should deprecated eventually:

- torch._dynamo.external_utils.is_compiling()
- torch._utils.is_compiling()

Example:

```
>>> def forward(self, x):
>>> if not torch.compiler.is_compiling():
>>> pass # ...logic that is not needed in a compiled/traced graph...
>>>
>>> # ...rest of the function...
```

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)