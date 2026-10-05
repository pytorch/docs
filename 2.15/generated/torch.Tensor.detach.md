# torch.Tensor.detach

Tensor.detach()

Returns a new Tensor, detached from the current graph.

The result will never require gradient.

This method also affects forward mode AD gradients and the result will never
have forward mode AD gradients.

Note

Returned Tensor shares the same storage with the original one.
In-place modifications on either of them will be seen, and may trigger
errors in correctness checks.