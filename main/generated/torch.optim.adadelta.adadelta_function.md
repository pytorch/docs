# torch.optim.adadelta.adadelta

torch.optim.adadelta.adadelta(*params*, *grads*, *square_avgs*, *acc_deltas*, *state_steps*, *capturable=False*, *foreach=None*, *differentiable=False*, *has_complex=False*, ***, *lr*, *rho*, *eps*, *weight_decay*, *maximize*)[[source]](https://github.com/pytorch/pytorch/blob/c9fded8194d3b089ed610b586eb746a6e74c6616/torch/optim/adadelta.py#L412)

Functional API that performs Adadelta algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`Adadelta`](torch.optim.Adadelta.html#torch.optim.Adadelta) for algorithm
details.