# torch.autograd.graph.Node.name

*abstract*Node.name()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/autograd/graph.py#L60)

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