# torch.autograd.graph.Node.register_hook

*abstract*Node.register_hook(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/c8080db61856d74ad76795af1c6aa1fd41b7b862/torch/autograd/graph.py#L96)

Register a backward hook.

The hook will be called every time a gradient with respect to the
Node is computed. The hook should have the following signature:

```
hook(grad_inputs: Tuple[Tensor], grad_outputs: Tuple[Tensor]) -> Tuple[Tensor] or None
```

The hook should not modify its argument, but it can optionally return
a new gradient which will be used in place of `grad_inputs`.

This function returns a handle with a method `handle.remove()`
that removes the hook from the module.

Note

See [Backward Hooks execution](../notes/autograd.html#backward-hooks-execution) for more information on how when this hook
is executed, and how its execution is ordered relative to other hooks.

Note

In the rare case where the hook is registered while the Node has already
begun execution, there is no longer any guarantee on `grad_outputs`
content (it might be as usual or empty depending on other factors). The
hook can still optionally return a new gradient to be used in place of
`grad_inputs` independent of `grad_outputs`.

Example:

```
>>> import torch
>>> a = torch.tensor([0., 0., 0.], requires_grad=True)
>>> b = a.clone()
>>> assert isinstance(b.grad_fn, torch.autograd.graph.Node)
>>> handle = b.grad_fn.register_hook(lambda gI, gO: (gO[0] * 2,))
>>> b.sum().backward(retain_graph=True)
>>> print(a.grad)
tensor([2., 2., 2.])
>>> handle.remove() # Removes the hook
>>> a.grad = None
>>> b.sum().backward(retain_graph=True)
>>> print(a.grad)
tensor([1., 1., 1.])
```

Return type:

*RemovableHandle*