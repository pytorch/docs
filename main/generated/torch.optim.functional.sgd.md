# torch.optim.functional.sgd

torch.optim.functional.sgd(*params*, *d_p_list*, *momentum_buffer_list*, *has_sparse_grad=False*, *foreach=None*, *fused=None*, *grad_scale=None*, *found_inf=None*, ***, *weight_decay*, *momentum*, *lr*, *dampening*, *nesterov*, *maximize*)[[source]](https://github.com/pytorch/pytorch/blob/13818df097cc56c9a2a860678049f2a42a008853/torch/optim/sgd.py#L253)

Functional API that performs SGD algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`SGD`](torch.optim.SGD.html#torch.optim.SGD) for algorithm
details.