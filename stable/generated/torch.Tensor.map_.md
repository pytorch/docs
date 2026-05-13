# torch.Tensor.map_

Tensor.map_(*tensor*, *callable*)

Applies `callable` for each element in `self` tensor and the given
[`tensor`](torch.tensor.html#torch.tensor) and stores the results in `self` tensor. `self` tensor and
the given [`tensor`](torch.tensor.html#torch.tensor) must be [broadcastable](../notes/broadcasting.html#broadcasting-semantics).

The `callable` should have the signature:

```
def callable(a, b) -> number
```