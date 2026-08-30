# torch.optim.functional.asgd

torch.optim.functional.asgd(*params*, *grads*, *axs*, *mus*, *etas*, *state_steps*, *foreach=None*, *maximize=False*, *differentiable=False*, *capturable=False*, *has_complex=False*, ***, *lambd*, *lr*, *t0*, *alpha*, *weight_decay*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/optim/asgd.py#L428)

Functional API that performs ASGD algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`ASGD`](torch.optim.ASGD.html#torch.optim.ASGD) for algorithm
details.