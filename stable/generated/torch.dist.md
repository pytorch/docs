# torch.dist

torch.dist(*input*, *other*, *p=2*) → [Tensor](../tensors.html#torch.Tensor)

Returns the p-norm of (`input` - `other`)

The shapes of `input` and `other` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the Right-hand-side input tensor
- **p** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - the norm to be computed

Example:

```
>>> x = torch.randn(4)
>>> x
tensor([-1.5393, -0.8675, 0.5916, 1.6321])
>>> y = torch.randn(4)
>>> y
tensor([ 0.0967, -1.0511, 0.6295, 0.8360])
>>> torch.dist(x, y, 3.5)
tensor(1.6727)
>>> torch.dist(x, y, 3)
tensor(1.6973)
>>> torch.dist(x, y, 0)
tensor(4.)
>>> torch.dist(x, y, 1)
tensor(2.6537)
```