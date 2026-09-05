# torch.optim.adam.adam

torch.optim.adam.adam(*params*, *grads*, *exp_avgs*, *exp_avg_sqs*, *max_exp_avg_sqs*, *state_steps*, *foreach=None*, *capturable=False*, *differentiable=False*, *fused=None*, *grad_scale=None*, *found_inf=None*, *has_complex=False*, *decoupled_weight_decay=False*, ***, *amsgrad*, *beta1*, *beta2*, *lr*, *weight_decay*, *eps*, *maximize*)[[source]](https://github.com/pytorch/pytorch/blob/13818df097cc56c9a2a860678049f2a42a008853/torch/optim/adam.py#L903)

Functional API that performs Adam algorithm computation.

This function updates the provided parameters and optimizer state in place.
The caller must initialize and retain optimizer state. Unless intentionally
constructing a differentiable update with a supported `differentiable=True`
argument, call this function under [`torch.no_grad`](torch.no_grad.html#torch.no_grad).
See [Functional optimizer API](../optim.html#functional-optimizer-api) for the common functional optimizer
contract and examples, and [`Adam`](torch.optim.Adam.html#torch.optim.Adam) for algorithm
details.

Note

With `fused=True`, CUDA supports FP32 parameters and gradients with
BF16 moment buffers. See [AdamW with BF16 optimizer state](../optim.html#functional-adamw-bf16-state) for an example.