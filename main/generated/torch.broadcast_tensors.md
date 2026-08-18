# torch.broadcast_tensors

torch.broadcast_tensors(**tensors*) → List of Tensors[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/functional.py#L47)

Broadcasts the given tensors according to [Broadcasting semantics](../notes/broadcasting.html#broadcasting-semantics).

Parameters:

***tensors** - any number of tensors of the same type

Warning

More than one element of a broadcasted tensor may refer to a single
memory location. As a result, in-place operations (especially ones that
are vectorized) may result in incorrect behavior. If you need to write
to the tensors, please clone them first.

Example:

```
>>> x = torch.arange(3).view(1, 3)
>>> y = torch.arange(2).view(2, 1)
>>> a, b = torch.broadcast_tensors(x, y)
>>> a.size()
torch.Size([2, 3])
>>> a
tensor([[0, 1, 2],
 [0, 1, 2]])
```