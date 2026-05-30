# torch.fx.experimental.unification.variable.variables

torch.fx.experimental.unification.variable.variables(**variables*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/fx/experimental/unification/variable.py#L68)

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