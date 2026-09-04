# torch.fx.experimental.unification.variable.variables

torch.fx.experimental.unification.variable.variables(**variables*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/fx/experimental/unification/variable.py#L67)

Context manager for logic variables

Example

```
>>> from __future__ import with_statement
>>> with variables(1):
... print(isvar(1))
True
>>> print(isvar(1))
False
>>> # Normal approach
>>> from unification import unify
>>> x = var("x")
>>> unify(x, 1)
{~x: 1}
>>> # Context Manager approach
>>> with variables("x"):
... print(unify("x", 1))
{'x': 1}
```

Return type:

[Generator](torch.Generator.html#torch.Generator)[None, None, None]