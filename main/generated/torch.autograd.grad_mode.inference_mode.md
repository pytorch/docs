# inference_mode

*class*torch.autograd.grad_mode.inference_mode(*mode=True*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/autograd/grad_mode.py#L213)

Context manager that enables or disables inference mode.

InferenceMode is analogous to [`no_grad`](torch.no_grad.html#torch.no_grad) and should be used
when you are certain your operations will not interact with autograd
(e.g., during data loading or model evaluation). Compared to
[`no_grad`](torch.no_grad.html#torch.no_grad), it removes additional overhead by disabling view
tracking and version counter bumps. It is also more restrictive, in
that tensors created in this mode cannot be used in computations
recorded by autograd.

This context manager is thread-local; it does not affect computation
in other threads.

Also functions as a decorator.

Note

Inference mode is one of several mechanisms that can locally enable
or disable gradients. See [Locally disabling gradient computation](../notes/autograd.html#locally-disable-grad-doc) for a
comparison. If avoiding the use of tensors created in inference mode
in autograd-tracked regions is difficult, consider benchmarking your
code with and without inference mode to weigh the performance benefits
against the trade-offs. You can always use [`no_grad`](torch.no_grad.html#torch.no_grad) instead.

Note

Unlike some other mechanisms that locally enable or disable grad,
entering inference_mode also disables [forward-mode AD](../autograd.html#forward-mode-ad).

Warning

inference_mode does NOT automatically set the model to evaluation mode.
For proper inference behavior (e.g., disabling dropout, using running statistics
in batch normalization), you must explicitly set your model to evaluation mode using
model.eval() in addition to using this context manager.

Parameters:

**mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*or**function*) - Either a boolean flag to enable or disable
inference mode, or a Python function to decorate with inference
mode enabled.

Example::

```
>>> import torch
>>> x = torch.ones(1, 2, 3, requires_grad=True)
>>> with torch.inference_mode():
... y = x * x
>>> y.requires_grad
False
>>> y._version
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
RuntimeError: Inference tensors do not track version counter.
>>> @torch.inference_mode()
... def func(x):
... return x * x
>>> out = func(x)
>>> out.requires_grad
False
>>> @torch.inference_mode()
... def doubler(x):
... return x * 2
>>> out = doubler(x)
>>> out.requires_grad
False
```

clone()[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/autograd/grad_mode.py#L297)

Create a copy of this class

Return type:

*inference_mode*