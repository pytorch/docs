# torch.optim.rmsprop.rmsprop

torch.optim.rmsprop.rmsprop(*params*, *grads*, *square_avgs*, *grad_avgs*, *momentum_buffer_list*, *state_steps*, *foreach=None*, *maximize=False*, *differentiable=False*, *capturable=False*, *has_complex=False*, ***, *lr*, *alpha*, *eps*, *weight_decay*, *momentum*, *centered*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/optim/rmsprop.py#L479)

Functional API that performs RMSprop algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`RMSprop`](torch.optim.RMSprop.html#torch.optim.RMSprop) for algorithm
details.