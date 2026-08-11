# torch.Tensor.requires_grad_

Tensor.requires_grad_(*requires_grad=True*) → [Tensor](../tensors.html#torch.Tensor)

Change if autograd should record operations on this tensor: sets this tensor's
[`requires_grad`](torch.Tensor.requires_grad.html#torch.Tensor.requires_grad) attribute in-place. Returns this tensor.

`requires_grad_()`'s main use case is to tell autograd to begin recording
operations on a Tensor `tensor`. If `tensor` has `requires_grad=False`
(because it was obtained through a DataLoader, or required preprocessing or
initialization), `tensor.requires_grad_()` makes it so that autograd will
begin to record operations on `tensor`.

Parameters:

**requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If autograd should record operations on this tensor.
Default: `True`.

Example:

```
>>> # Let's say we want to preprocess some saved weights and use
>>> # the result as new weights.
>>> saved_weights = [0.1, 0.2, 0.3, 0.25]
>>> loaded_weights = torch.tensor(saved_weights)
>>> weights = preprocess(loaded_weights) # some function
>>> weights
tensor([-0.5503, 0.4926, -2.1158, -0.8303])

>>> # Now, start to record operations done to weights
>>> weights.requires_grad_()
>>> out = weights.pow(2).sum()
>>> out.backward()
>>> weights.grad
tensor([-1.1007, 0.9853, -4.2316, -1.6606])
```