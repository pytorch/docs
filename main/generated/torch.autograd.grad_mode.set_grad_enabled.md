# set_grad_enabled

*class*torch.autograd.grad_mode.set_grad_enabled(*mode*)[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/autograd/grad_mode.py#L144)

Context-manager that sets gradient calculation on or off.

`set_grad_enabled` will enable or disable grads based on its argument `mode`.
It can be used as a context-manager or as a function.

This context manager is thread local; it will not affect computation
in other threads.

Parameters:

**mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Flag whether to enable grad (`True`), or disable
(`False`). This can be used to conditionally enable
gradients.

Note

set_grad_enabled is one of several mechanisms that can enable or
disable gradients locally see [Locally disabling gradient computation](../notes/autograd.html#locally-disable-grad-doc) for
more information on how they compare.

Note

This API does not apply to [forward-mode AD](../autograd.html#forward-mode-ad).

Example::

```
>>> x = torch.tensor([1.], requires_grad=True)
>>> is_train = False
>>> with torch.set_grad_enabled(is_train):
... y = x * 2
>>> y.requires_grad
False
>>> _ = torch.set_grad_enabled(True)
>>> y = x * 2
>>> y.requires_grad
True
>>> _ = torch.set_grad_enabled(False)
>>> y = x * 2
>>> y.requires_grad
False
```

clone()[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/autograd/grad_mode.py#L206)

Create a copy of this class

Return type:

*set_grad_enabled*