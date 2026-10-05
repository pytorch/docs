# torch.Tensor.grad

Tensor.grad

This attribute is `None` by default and becomes a Tensor the first time a call to
[`backward()`](torch.Tensor.backward.html#torch.Tensor.backward) computes gradients for `self`.
The attribute will then contain the gradients computed and future calls to
[`backward()`](torch.Tensor.backward.html#torch.Tensor.backward) will accumulate (add) gradients into it.