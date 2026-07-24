# torch.autograd.graph.Node.name

*abstract*Node.name()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/autograd/graph.py#L58)

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