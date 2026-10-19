# torch.optim.functional.nadam

torch.optim.functional.nadam(*params*, *grads*, *exp_avgs*, *exp_avg_sqs*, *mu_products*, *state_steps*, *decoupled_weight_decay=False*, *foreach=None*, *capturable=False*, *differentiable=False*, *has_complex=False*, *maximize=False*, ***, *beta1*, *beta2*, *lr*, *weight_decay*, *momentum_decay*, *eps*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/optim/nadam.py#L607)

Functional API that performs NAdam algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`NAdam`](torch.optim.NAdam.html#torch.optim.NAdam) for algorithm
details.