# torch.Tensor.masked_scatter_

Tensor.masked_scatter_(*mask*, *source*)

Copies elements from `source` into `self` tensor at positions where
the `mask` is True. Elements from `source` are copied into `self`
starting at position 0 of `source` and continuing in order one-by-one for each
occurrence of `mask` being True.
The shape of `mask` must be [broadcastable](../notes/broadcasting.html#broadcasting-semantics)
with the shape of the underlying tensor. The `source` should have at least
as many elements as the number of ones in `mask`.

Parameters:

- **mask** (*BoolTensor*) - the boolean mask
- **source** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor to copy from

Note

The `mask` operates on the `self` tensor, not on the given
`source` tensor.

Example

```
>>> self = torch.tensor([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
>>> mask = torch.tensor(
... [[0, 0, 0, 1, 1], [1, 1, 0, 1, 1]],
... dtype=torch.bool,
... )
>>> source = torch.tensor([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
>>> self.masked_scatter_(mask, source)
tensor([[0, 0, 0, 0, 1],
 [2, 3, 0, 4, 5]])
```