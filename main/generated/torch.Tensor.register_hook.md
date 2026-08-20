# torch.Tensor.register_hook

Tensor.register_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/_tensor.py#L655)

Registers a backward hook.

The hook will be called every time a gradient with respect to the
Tensor is computed. The hook should have the following signature:

```
hook(grad) -> Tensor or None
```

The hook should not modify its argument, but it can optionally return
a new gradient which will be used in place of [`grad`](torch.Tensor.grad.html#torch.Tensor.grad).

This function returns a handle with a method `handle.remove()`
that removes the hook from the module.

Note

See [Backward Hooks execution](../notes/autograd.html#backward-hooks-execution) for more information on how when this hook
is executed, and how its execution is ordered relative to other hooks.

Example:

```
>>> v = torch.tensor([0., 0., 0.], requires_grad=True)
>>> h = v.register_hook(lambda grad: grad * 2) # double the gradient
>>> v.backward(torch.tensor([1., 2., 3.]))
>>> v.grad

 2
 4
 6
[torch.FloatTensor of size (3,)]

>>> h.remove() # removes the hook
```