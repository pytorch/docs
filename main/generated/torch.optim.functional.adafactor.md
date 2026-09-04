# torch.optim.functional.adafactor

torch.optim.functional.adafactor(*params*, *grads*, *row_vars*, *col_vars*, *variances*, *state_steps*, *foreach=None*, *grad_scale=None*, *found_inf=None*, *has_complex=False*, ***, *d*, *lr*, *beta2_decay*, *weight_decay*, *eps1*, *eps2*, *maximize*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/optim/_adafactor.py#L606)

Functional API that performs Adafactor algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`Adafactor`](torch.optim.Adafactor.html#torch.optim.Adafactor) for algorithm
details.