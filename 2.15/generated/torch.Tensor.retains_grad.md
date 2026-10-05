# torch.Tensor.retains_grad

Tensor.retains_grad

Is `True` if this Tensor is non-leaf and its [`grad`](torch.Tensor.grad.html#torch.Tensor.grad) is enabled to be
populated during [`backward()`](torch.Tensor.backward.html#torch.Tensor.backward), `False` otherwise.