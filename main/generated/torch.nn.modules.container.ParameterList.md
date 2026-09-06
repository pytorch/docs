# ParameterList

*class*torch.nn.modules.container.ParameterList(*values=None*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/nn/modules/container.py#L652)

Holds parameters in a list.

[`ParameterList`](torch.nn.ParameterList.html#torch.nn.ParameterList) can be used like a regular Python
list, but Tensors that are `Parameter` are properly registered,
and will be visible by all [`Module`](torch.nn.Module.html#torch.nn.Module) methods.

Note that the constructor, assigning an element of the list, the
[`append()`](torch.nn.ParameterList.html#torch.nn.ParameterList.append) method and the [`extend()`](torch.nn.ParameterList.html#torch.nn.ParameterList.extend)
method will convert any [`Tensor`](../tensors.html#torch.Tensor) into `Parameter`.

Parameters:

**parameters** (*iterable**,**optional*) - an iterable of elements to add to the list.

Example:

```
class MyModule(nn.Module):
 def __init__(self) -> None:
 super().__init__()
 self.params = nn.ParameterList(
 [nn.Parameter(torch.randn(10, 10)) for i in range(10)]
 )

 def forward(self, x):
 # ParameterList can act as an iterable, or be indexed using ints
 for i, p in enumerate(self.params):
 x = self.params[i // 2].mm(x) + p.mm(x)
 return x
```

append(*value*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/nn/modules/container.py#L740)

Append a given value at the end of the list.

Parameters:

**value** (*Any*) - value to append

Return type:

*Self*

extend(*values*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/nn/modules/container.py#L751)

Append values from a Python iterable to the end of the list.

Parameters:

**values** (*iterable*) - iterable of values to append

Return type:

Self

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/nn/modules/container.py#L769)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)