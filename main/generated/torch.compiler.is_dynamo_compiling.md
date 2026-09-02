# torch.compiler.is_dynamo_compiling

torch.compiler.is_dynamo_compiling()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/compiler/__init__.py#L717)

Indicates whether a graph is traced via TorchDynamo.

It's stricter than is_compiling() flag, as it would only be set to True when
TorchDynamo is used.

Example:

```
>>> def forward(self, x):
>>> if not torch.compiler.is_dynamo_compiling():
>>> pass # ...logic that is not needed in a TorchDynamo-traced graph...
>>>
>>> # ...rest of the function...
```

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)