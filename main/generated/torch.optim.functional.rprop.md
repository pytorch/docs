# torch.optim.functional.rprop

torch.optim.functional.rprop(*params*, *grads*, *prevs*, *step_sizes*, *state_steps*, *foreach=None*, *capturable=False*, *maximize=False*, *differentiable=False*, *has_complex=False*, ***, *step_size_min*, *step_size_max*, *etaminus*, *etaplus*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/optim/rprop.py#L413)

Functional API that performs Rprop algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`Rprop`](torch.optim.Rprop.html#torch.optim.Rprop) for algorithm
details.