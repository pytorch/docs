# torch.optim.adagrad.adagrad

torch.optim.adagrad.adagrad(*params*, *grads*, *state_sums*, *state_steps*, *fused=None*, *grad_scale=None*, *found_inf=None*, *has_sparse_grad=False*, *foreach=None*, *differentiable=False*, *has_complex=False*, ***, *lr*, *weight_decay*, *lr_decay*, *eps*, *maximize*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/optim/adagrad.py#L286)

Functional API that performs Adagrad algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`Adagrad`](torch.optim.Adagrad.html#torch.optim.Adagrad) for algorithm
details.