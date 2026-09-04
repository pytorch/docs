# torch.optim.functional.adagrad

torch.optim.functional.adagrad(*params*, *grads*, *state_sums*, *state_steps*, *fused=None*, *grad_scale=None*, *found_inf=None*, *has_sparse_grad=False*, *foreach=None*, *differentiable=False*, *has_complex=False*, ***, *lr*, *weight_decay*, *lr_decay*, *eps*, *maximize*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/optim/adagrad.py#L286)

Functional API that performs Adagrad algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`Adagrad`](torch.optim.Adagrad.html#torch.optim.Adagrad) for algorithm
details.