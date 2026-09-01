# torch.optim.functional.muon

torch.optim.functional.muon(*params*, *grads*, *muon_momentum_bufs*, ***, *foreach=None*, *lr*, *weight_decay*, *momentum*, *nesterov*, *ns_coefficients*, *ns_steps*, *eps*, *adjust_lr_fn*, *has_complex*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/optim/_muon.py#L355)

Functional API that performs Muon algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`Muon`](torch.optim.Muon.html#torch.optim.Muon) for algorithm
details.