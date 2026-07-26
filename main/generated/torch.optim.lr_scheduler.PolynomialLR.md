# PolynomialLR

*class*torch.optim.lr_scheduler.PolynomialLR(*optimizer*, *total_iters=5*, *power=1.0*, *last_epoch=-1*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/optim/lr_scheduler.py#L1237)

Decays the learning rate of each parameter group using a polynomial function in the given total_iters.

When last_epoch=-1, sets initial lr as lr.

Parameters:

- **optimizer** ([*Optimizer*](../optim.html#torch.optim.Optimizer)) - Wrapped optimizer.
- **total_iters** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The number of steps that the scheduler decays the learning rate. Default: 5.
- **power** ([*float*](https://docs.python.org/3/library/functions.html#float)) - The power of the polynomial. Default: 1.0.

Example

```
>>> # Assuming optimizer uses lr = 0.05 for all groups
>>> # lr = 0.0490 if epoch == 0
>>> # lr = 0.0481 if epoch == 1
>>> # lr = 0.0472 if epoch == 2
>>> # ...
>>> # lr = 0.0 if epoch >= 50
>>> scheduler = PolynomialLR(optimizer, total_iters=50, power=0.9)
>>> for epoch in range(100):
>>> train(...)
>>> validate(...)
>>> scheduler.step()
```

![../_images/PolynomialLR.png](../_images/PolynomialLR.png)

get_last_lr()[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/optim/lr_scheduler.py#L201)

Get the most recent learning rates computed by this scheduler.

Returns:

A [`list`](https://docs.python.org/3/library/stdtypes.html#list) of learning rates with entries
for each of the optimizer's
`param_groups`, with the same types as
their `group["lr"]`s.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[float](https://docs.python.org/3/library/functions.html#float) | [Tensor](../tensors.html#torch.Tensor)]

Note

The returned [`Tensor`](../tensors.html#torch.Tensor)s are copies, and never alias
the optimizer's `group["lr"]`s.

get_lr()[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/optim/lr_scheduler.py#L1275)

Compute the next learning rate for each of the optimizer's
`param_groups`.

Scales the `group["lr"]`s in the optimizer's
`param_groups` such that the learning rates
follow

base_lr⋅(1−last_epochtotal_iters)power\texttt{base\_lr} \cdot \left(1 - \frac{\texttt{last\_epoch}}
{\texttt{total\_iters}} \right)^\texttt{power}

base_lr⋅(1−total_iterslast_epoch​)power

Returns the current learning rates unchanged after `total_iters`
is reached.

Returns:

A [`list`](https://docs.python.org/3/library/stdtypes.html#list) of learning rates for each of
the optimizer's `param_groups` with the
same types as their current `group["lr"]`s.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[float](https://docs.python.org/3/library/functions.html#float) | [Tensor](../tensors.html#torch.Tensor)]

Note

If you're trying to inspect the most recent learning rate, use
`get_last_lr()` instead.

Note

The returned [`Tensor`](../tensors.html#torch.Tensor)s are copies, and never alias
the optimizer's `group["lr"]`s.

load_state_dict(*state_dict*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/optim/lr_scheduler.py#L192)

Load the scheduler's state.

Parameters:

**state_dict** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - scheduler state. Should be an object returned
from a call to `state_dict()`.

state_dict()[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/optim/lr_scheduler.py#L182)

Return the state of the scheduler as a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict).

It contains an entry for every variable in `self.__dict__` which
is not the optimizer.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

step(*epoch=None*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/optim/lr_scheduler.py#L238)

Step the scheduler.

Parameters:

**epoch** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) -

Deprecated since version 1.4: If provided, sets `last_epoch` to `epoch` and uses
`_get_closed_form_lr()` if it is available. This is not
universally supported. Use `step()` without arguments
instead.

Note

Call this method after calling the optimizer's
[`step()`](torch.optim.Optimizer.step.html#torch.optim.Optimizer.step).