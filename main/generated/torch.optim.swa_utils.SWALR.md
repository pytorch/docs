# SWALR

*class*torch.optim.swa_utils.SWALR(*optimizer*, *swa_lr*, *anneal_epochs=10*, *anneal_strategy='cos'*, *last_epoch=-1*)[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/optim/swa_utils.py#L430)

Anneals the learning rate in each parameter group to a fixed value.

This learning rate scheduler is meant to be used with Stochastic Weight
Averaging (SWA) method (see torch.optim.swa_utils.AveragedModel).

Parameters:

- **optimizer** ([*torch.optim.Optimizer*](../optim.html#torch.optim.Optimizer)) - wrapped optimizer
- **swa_lrs** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)) - the learning rate value for all param groups
together or separately for each group.
- **annealing_epochs** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of epochs in the annealing phase
(default: 10)
- **annealing_strategy** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - "cos" or "linear"; specifies the annealing
strategy: "cos" for cosine annealing, "linear" for linear annealing
(default: "cos")
- **last_epoch** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the index of the last epoch (default: -1)

The `SWALR` scheduler can be used together with other
schedulers to switch to a constant learning rate late in the training
as in the example below.

Example

```
>>> loader, optimizer, model = ...
>>> lr_lambda = lambda epoch: 0.9
>>> scheduler = torch.optim.lr_scheduler.MultiplicativeLR(optimizer,
>>> lr_lambda=lr_lambda)
>>> swa_scheduler = torch.optim.swa_utils.SWALR(optimizer,
>>> anneal_strategy="linear", anneal_epochs=20, swa_lr=0.05)
>>> swa_start = 160
>>> for i in range(300):
>>> for input, target in loader:
>>> optimizer.zero_grad()
>>> loss_fn(model(input), target).backward()
>>> optimizer.step()
>>> if i > swa_start:
>>> swa_scheduler.step()
>>> else:
>>> scheduler.step()
```

get_last_lr()[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/optim/lr_scheduler.py#L201)

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

get_lr()[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/optim/swa_utils.py#L512)

Compute the next learning rate for each of the optimizer's
`param_groups`.

Uses `anneal_func` to interpolate between each group's
`group["lr"]` and `group["swa_lr"]` over `anneal_epochs`
epochs. Once `anneal_epochs` is reached, keeps the learning rate
fixed at `group["swa_lr"]`.

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

load_state_dict(*state_dict*)[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/optim/swa_utils.py#L583)

Load the scheduler's state.

Parameters:

**state_dict** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - scheduler state. Should be an object returned
from a call to `state_dict()`.

state_dict()[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/optim/swa_utils.py#L570)

Return the state of the scheduler as a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict).

It contains an entry for every variable in self.__dict__ which
is not the optimizer or anneal_func.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

step(*epoch=None*)[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/optim/lr_scheduler.py#L238)

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