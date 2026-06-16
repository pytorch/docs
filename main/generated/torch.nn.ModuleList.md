# ModuleList

*class*torch.nn.ModuleList(*modules=None*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/nn/modules/container.py#L335)

Holds submodules in a list.

`ModuleList` can be indexed like a regular Python list, but
modules it contains are properly registered, and will be visible by all
[`Module`](torch.nn.Module.html#torch.nn.Module) methods.

Parameters:

**modules** (*iterable**,**optional*) - an iterable of modules to add

Example:

```
class MyModule(nn.Module):
 def __init__(self) -> None:
 super().__init__()
 self.linears = nn.ModuleList([nn.Linear(10, 10) for i in range(10)])

 def forward(self, x):
 # ModuleList can act as an iterable, or be indexed using ints
 for i, l in enumerate(self.linears):
 x = self.linears[i // 2](x) + l(x)
 return x
```

append(*module*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/nn/modules/container.py#L472)

Append a given module to the end of the list.

Parameters:

**module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module to append

Return type:

*Self*

extend(*modules*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/nn/modules/container.py#L486)

Append modules from a Python iterable to the end of the list.

Parameters:

**modules** (*iterable*) - iterable of modules to append

Return type:

Self

insert(*index*, *module*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/nn/modules/container.py#L461)

Insert a given module before a given index in the list.

Parameters:

- **index** ([*int*](https://docs.python.org/3/library/functions.html#int)) - index to insert.
- **module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module to insert