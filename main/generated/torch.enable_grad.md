# enable_grad

*class*torch.enable_grad(*orig_func: F*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/autograd/grad_mode.py#L89)

*class*torch.enable_grad(*orig_func: [None](https://docs.python.org/3/library/constants.html#None) = None*)

Context-manager that enables gradient calculation.

Enables gradient calculation, if it has been disabled via [`no_grad`](torch.no_grad.html#torch.no_grad)
or `set_grad_enabled`.

This context manager is thread local; it will not affect computation
in other threads.

Also functions as a decorator.

Note

enable_grad is one of several mechanisms that can enable or
disable gradients locally see [Locally disabling gradient computation](../notes/autograd.html#locally-disable-grad-doc) for
more information on how they compare.

Note

This API does not apply to [forward-mode AD](../autograd.html#forward-mode-ad).

Example::

```
>>> x = torch.tensor([1.], requires_grad=True)
>>> with torch.no_grad():
... with torch.enable_grad():
... y = x * 2
>>> y.requires_grad
True
>>> y.backward()
>>> x.grad
tensor([2.])
>>> @torch.enable_grad()
... def doubler(x):
... return x * 2
>>> with torch.no_grad():
... z = doubler(x)
>>> z.requires_grad
True
>>> @torch.enable_grad()
... def tripler(x):
... return x * 3
>>> with torch.no_grad():
... z = tripler(x)
>>> z.requires_grad
True
```

Return type:

*Self* | *F*