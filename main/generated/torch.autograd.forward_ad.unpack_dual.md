# torch.autograd.forward_ad.unpack_dual

torch.autograd.forward_ad.unpack_dual(*tensor*, ***, *level=None*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/autograd/forward_ad.py#L151)

Unpack a "dual tensor" to get both its Tensor value and its forward AD gradient.

The result is a namedtuple `(primal, tangent)` where `primal` is a view of
`tensor`'s primal and `tangent` is `tensor`'s tangent as-is.
Neither of these tensors can be dual tensor of level `level`.

This function is backward differentiable.

Example:

```
>>> with dual_level():
... inp = make_dual(x, x_t)
... out = f(inp)
... y, jvp = unpack_dual(out)
... jvp = unpack_dual(out).tangent
```

Please see the [forward-mode AD tutorial](https://pytorch.org/tutorials/intermediate/forward_ad_usage.html)
for detailed steps on how to use this API.