# torch.optim.radam.radam

torch.optim.radam.radam(*params*, *grads*, *exp_avgs*, *exp_avg_sqs*, *state_steps*, *decoupled_weight_decay=False*, *foreach=None*, *differentiable=False*, *capturable=False*, *has_complex=False*, *maximize=False*, ***, *beta1*, *beta2*, *lr*, *weight_decay*, *eps*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/optim/radam.py#L567)

Functional API that performs RAdam algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`RAdam`](torch.optim.RAdam.html#torch.optim.RAdam) for algorithm
details.