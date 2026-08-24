# torch.autograd.graph.Node.name

*abstract*Node.name()[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/autograd/graph.py#L59)

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