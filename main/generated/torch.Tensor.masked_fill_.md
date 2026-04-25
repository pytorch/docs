# torch.Tensor.masked_fill_

Tensor.masked_fill_(*mask*, *value*)

Fills elements of `self` tensor with `value` where `mask` is
True. The shape of `mask` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics) with the shape of the underlying
tensor.

Parameters:

- **mask** (*BoolTensor*) - the boolean mask
- **value** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the value to fill in with