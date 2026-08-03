# torch.autograd.forward_ad.unpack_dual

torch.autograd.forward_ad.unpack_dual(*tensor*, ***, *level=None*)[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/autograd/forward_ad.py#L151)

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