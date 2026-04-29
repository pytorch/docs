# ModuleDict

*class*torch.nn.ModuleDict(*modules=None*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/nn/modules/container.py#L505)

Holds submodules in a dictionary.

`ModuleDict` can be indexed like a regular Python dictionary,
but modules it contains are properly registered, and will be visible by all
[`Module`](torch.nn.Module.html#torch.nn.Module) methods.

`ModuleDict` is an **ordered** dictionary that respects

- the order of insertion, and
- in `update()`, the order of the merged
`OrderedDict`, `dict` or another
`ModuleDict` (the argument to
`update()`).

Note that `update()` with other unordered mapping
types does not preserve the order of the merged mapping.

Parameters:

**modules** (*iterable**,**optional*) - a mapping (dictionary) of (string: module)
or an iterable of key-value pairs of type (string, module)

Example:

```
class MyModule(nn.Module):
 def __init__(self) -> None:
 super().__init__()
 self.choices = nn.ModuleDict(
 {"conv": nn.Conv2d(10, 10, 3), "pool": nn.MaxPool2d(3)}
 )
 self.activations = nn.ModuleDict(
 [["lrelu", nn.LeakyReLU()], ["prelu", nn.PReLU()]]
 )

 def forward(self, x, choice, act):
 x = self.choices[choice](x)
 x = self.activations[act](x)
 return x
```

clear()[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/nn/modules/container.py#L575)

Remove all items from the ModuleDict.

items()[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/nn/modules/container.py#L594)

Return an iterable of the ModuleDict key/value pairs.

Return type:

[*ItemsView*](https://docs.python.org/3/library/collections.abc.html#collections.abc.ItemsView)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Module*](torch.nn.Module.html#torch.nn.Module)]

keys()[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/nn/modules/container.py#L589)

Return an iterable of the ModuleDict keys.

Return type:

[*KeysView*](https://docs.python.org/3/library/collections.abc.html#collections.abc.KeysView)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

pop(*key*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/nn/modules/container.py#L579)

Remove key from the ModuleDict and return its module.

Parameters:

**key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - key to pop from the ModuleDict

Return type:

[*Module*](torch.nn.Module.html#torch.nn.Module)

update(*modules*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/nn/modules/container.py#L604)

Update the `ModuleDict` with key-value pairs from a mapping, overwriting existing keys.

Note

If [`modules`](../nn.aliases.html#module-torch.nn.modules) is an `OrderedDict`, a `ModuleDict`, or
an iterable of key-value pairs, the order of new elements in it is preserved.

Parameters:

**modules** (*iterable*) - a mapping (dictionary) from string to [`Module`](torch.nn.Module.html#torch.nn.Module),
or an iterable of key-value pairs of type (string, [`Module`](torch.nn.Module.html#torch.nn.Module))

values()[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/nn/modules/container.py#L599)

Return an iterable of the ModuleDict values.

Return type:

[*ValuesView*](https://docs.python.org/3/library/collections.abc.html#collections.abc.ValuesView)[[*Module*](torch.nn.Module.html#torch.nn.Module)]