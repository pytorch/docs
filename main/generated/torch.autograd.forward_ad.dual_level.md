# dual_level

*class*torch.autograd.forward_ad.dual_level[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/autograd/forward_ad.py#L185)

Context-manager for forward AD, where all forward AD computation must occur within the `dual_level` context.

Note

The `dual_level` context appropriately enters and exit the dual level to
controls the current forward AD level, which is used by default by the other
functions in this API.

We currently don't plan to support nested `dual_level` contexts, however, so
only a single forward AD level is supported. To compute higher-order
forward grads, one can use [`torch.func.jvp()`](torch.func.jvp.html#torch.func.jvp).

Example:

```
>>> x = torch.tensor([1])
>>> x_t = torch.tensor([1])
>>> with dual_level():
... inp = make_dual(x, x_t)
... # Do computations with inp
... out = your_fn(inp)
... _, grad = unpack_dual(out)
>>> grad is None
False
>>> # After exiting the level, the grad is deleted
>>> _, grad_after = unpack_dual(out)
>>> grad is None
True
```

Please see the [forward-mode AD tutorial](https://pytorch.org/tutorials/intermediate/forward_ad_usage.html)
for detailed steps on how to use this API.