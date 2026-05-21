# no_grad

*class*torch.no_grad(*orig_func: F*)[[source]](https://github.com/pytorch/pytorch/blob/1af0b90bbfa06b98936ac35f25070579cffc8d74/torch/autograd/grad_mode.py#L22)

*class*torch.no_grad(*orig_func: [None](https://docs.python.org/3/library/constants.html#None) = None*)

Context-manager that disables gradient calculation.

Disabling gradient calculation is useful for inference, when you are sure
that you will not call [`Tensor.backward()`](torch.Tensor.backward.html#torch.Tensor.backward). It will reduce memory
consumption for computations that would otherwise have requires_grad=True.

In this mode, the result of every computation will have
requires_grad=False, even when the inputs have requires_grad=True.
There is an exception! All factory functions, or functions that create
a new Tensor and take a requires_grad kwarg, will NOT be affected by
this mode.

This context manager is thread local; it will not affect computation
in other threads.

Also functions as a decorator.

Note

No-grad is one of several mechanisms that can enable or
disable gradients locally see [Locally disabling gradient computation](../notes/autograd.html#locally-disable-grad-doc) for
more information on how they compare.

Note

This API does not apply to [forward-mode AD](../autograd.html#forward-mode-ad).
If you want to disable forward AD for a computation, you can unpack
your dual tensors.

Example::

```
>>> x = torch.tensor([1.], requires_grad=True)
>>> with torch.no_grad():
... y = x * 2
>>> y.requires_grad
False
>>> @torch.no_grad()
... def doubler(x):
... return x * 2
>>> z = doubler(x)
>>> z.requires_grad
False
>>> @torch.no_grad()
... def tripler(x):
... return x * 3
>>> z = tripler(x)
>>> z.requires_grad
False
>>> # factory function exception
>>> with torch.no_grad():
... a = torch.nn.Parameter(torch.rand(10))
>>> a.requires_grad
True
```