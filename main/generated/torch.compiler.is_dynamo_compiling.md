# torch.compiler.is_dynamo_compiling

torch.compiler.is_dynamo_compiling()[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/compiler/__init__.py#L721)

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

[bool](https://docs.python.org/3/builtins/functions.html#bool)