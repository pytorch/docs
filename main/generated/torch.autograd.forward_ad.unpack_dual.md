# torch.autograd.forward_ad.unpack_dual

torch.autograd.forward_ad.unpack_dual(*tensor*, ***, *level=None*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/autograd/forward_ad.py#L151)

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