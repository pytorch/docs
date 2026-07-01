# torch.autograd.forward_ad.make_dual

torch.autograd.forward_ad.make_dual(*tensor*, *tangent*, ***, *level=None*)[[source]](https://github.com/pytorch/pytorch/blob/df6ed392bccc6625dbf4f6a82bcecee03433aa18/torch/autograd/forward_ad.py#L77)

Associate a tensor value with its tangent to create a "dual tensor" for forward AD gradient computation.

The result is a new tensor aliased to `tensor` with `tangent` embedded
as an attribute as-is if it has the same storage layout or copied otherwise.
The tangent attribute can be recovered with [`unpack_dual()`](torch.autograd.forward_ad.unpack_dual.html#torch.autograd.forward_ad.unpack_dual).

This function is backward differentiable.

Given a function f whose jacobian is J, it allows one to compute the Jacobian-vector product (jvp)
between J and a given vector v as follows.

Example:

```
>>> with dual_level():
... inp = make_dual(x, v)
... out = f(inp)
... y, jvp = unpack_dual(out)
```

Please see the [forward-mode AD tutorial](https://pytorch.org/tutorials/intermediate/forward_ad_usage.html)
for detailed steps on how to use this API.