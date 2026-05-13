# torch.Tensor.copy_

Tensor.copy_(*src*, *non_blocking=False*) → [Tensor](../tensors.html#torch.Tensor)

Copies the elements from `src` into `self` tensor and returns
`self`.

The `src` tensor must be [broadcastable](../notes/broadcasting.html#broadcasting-semantics)
with the `self` tensor. It may be of a different data type or reside on a
different device.

Parameters:

- **src** ([*Tensor*](../tensors.html#torch.Tensor)) - the source tensor to copy from
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True` and this copy is between CPU and GPU,
the copy may occur asynchronously with respect to the host. For other
cases, this argument has no effect. Default: `False`