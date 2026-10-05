# torch.Tensor.masked_scatter

Tensor.masked_scatter(*mask*, *tensor*) → [Tensor](../tensors.html#torch.Tensor)

Out-of-place version of [`torch.Tensor.masked_scatter_()`](torch.Tensor.masked_scatter_.html#torch.Tensor.masked_scatter_)

Note

The inputs `self` and `mask`
[broadcast](../notes/broadcasting.html#broadcasting-semantics).

Example

```
>>> self = torch.tensor([0, 0, 0, 0, 0])
>>> mask = torch.tensor(
... [[0, 0, 0, 1, 1], [1, 1, 0, 1, 1]],
... dtype=torch.bool,
... )
>>> source = torch.tensor([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
>>> self.masked_scatter(mask, source)
tensor([[0, 0, 0, 0, 1],
 [2, 3, 0, 4, 5]])
```