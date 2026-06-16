# enforce_grad_layout_policy

*class*torch.autograd.grad_mode.enforce_grad_layout_policy(*enable=True*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/autograd/grad_mode.py#L356)

Context-manager that controls the gradient layout policy enforcement.

The gradient layout contract ensures that accumulated gradients have
strides matching their corresponding parameters (for non-overlapping
dense parameters) or are row-major contiguous (otherwise). This aids
performance in optimizers and distributed reducers.

When `enable=False`, the autograd engine relaxes this enforcement:

- Stealable gradients whose layout does *not* match the parameter can
still be stolen directly (avoiding an extra copy).
- The "grad and param do not obey the gradient layout contract" warning
is suppressed.

The logic that *creates* a brand-new gradient (e.g., cloning into the
correct layout when the gradient is not stealable) is **not** affected
by this flag.

This can be used as a context-manager or as a function. It is
thread-local and will not affect computation in other threads.

Parameters:

**enable** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to enforce the gradient layout contract
(`True`, default) or relax enforcement (`False`).

Example::

```
>>> import torch
>>> p = torch.empty(2, 3, 4).permute(2, 0, 1).requires_grad_()
>>> with torch.autograd.enforce_grad_layout_policy(False):
... (p * 2).sum().backward()
... # p.grad may now have the same strides as the incoming
... # gradient rather than being forced to match p's strides.
```

clone()[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/autograd/grad_mode.py#L407)

Create a copy of this class

Return type:

*enforce_grad_layout_policy*