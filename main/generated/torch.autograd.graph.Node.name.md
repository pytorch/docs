# torch.autograd.graph.Node.name

*abstract*Node.name()[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/autograd/graph.py#L60)

Return the name.

Example:

```
>>> import torch
>>> a = torch.tensor([0., 0., 0.], requires_grad=True)
>>> b = a.clone()
>>> assert isinstance(b.grad_fn, torch.autograd.graph.Node)
>>> print(b.grad_fn.name())
CloneBackward0
```

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)