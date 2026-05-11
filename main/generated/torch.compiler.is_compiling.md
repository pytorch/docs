# torch.compiler.is_compiling

torch.compiler.is_compiling()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/compiler/__init__.py#L475)

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

[bool](https://docs.python.org/3/library/functions.html#bool)