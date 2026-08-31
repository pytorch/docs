# torch.optim.rprop.rprop

torch.optim.rprop.rprop(*params*, *grads*, *prevs*, *step_sizes*, *state_steps*, *foreach=None*, *capturable=False*, *maximize=False*, *differentiable=False*, *has_complex=False*, ***, *step_size_min*, *step_size_max*, *etaminus*, *etaplus*)[[source]](https://github.com/pytorch/pytorch/blob/c9fded8194d3b089ed610b586eb746a6e74c6616/torch/optim/rprop.py#L413)

Functional API that performs Rprop algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`Rprop`](torch.optim.Rprop.html#torch.optim.Rprop) for algorithm
details.