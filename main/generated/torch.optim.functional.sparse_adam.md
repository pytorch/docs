# torch.optim.functional.sparse_adam

torch.optim.functional.sparse_adam(*params*, *grads*, *exp_avgs*, *exp_avg_sqs*, *state_steps*, ***, *eps*, *beta1*, *beta2*, *lr*, *maximize*)[[source]](https://github.com/pytorch/pytorch/blob/13818df097cc56c9a2a860678049f2a42a008853/torch/optim/_functional.py#L24)

Functional API that performs SparseAdam algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`SparseAdam`](torch.optim.SparseAdam.html#torch.optim.SparseAdam) for algorithm
details.

Note

`state_steps` must contain the current step value for each parameter.
This function reads these values but does not increment them; the caller must
increment each step before the corresponding update.