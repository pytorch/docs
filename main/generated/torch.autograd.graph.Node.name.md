# torch.autograd.graph.Node.name

*abstract*Node.name()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/autograd/graph.py#L57)

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

[str](https://docs.python.org/3/library/stdtypes.html#str)