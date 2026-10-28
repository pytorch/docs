# torch.Tensor.retain_grad

Tensor.retain_grad() → [None](https://docs.python.org/3/builtins/constants.html#None)

Enables this Tensor to have their [`grad`](torch.Tensor.grad.html#torch.Tensor.grad) populated during
[`backward()`](torch.Tensor.backward.html#torch.Tensor.backward). This is a no-op for leaf tensors.