# torch.autograd.function.FunctionCtx.mark_dirty

FunctionCtx.mark_dirty(**args*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/autograd/function.py#L158)

Mark given tensors as modified in an in-place operation.

This should be called at most once, in either the `setup_context()`
or `forward()` methods, and all arguments should be inputs.

Every tensor that's been modified in-place in a call to `forward()`
should be given to this function, to ensure correctness of our checks.
It doesn't matter whether the function is called before or after
modification.

Examples::

```
>>> class Inplace(Function):
>>> @staticmethod
>>> def forward(ctx, x):
>>> x_npy = x.numpy() # x_npy shares storage with x
>>> x_npy += 1
>>> ctx.mark_dirty(x)
>>> return x
>>>
>>> @staticmethod
>>> @once_differentiable
>>> def backward(ctx, grad_output):
>>> return grad_output
>>>
>>> a = torch.tensor(1., requires_grad=True, dtype=torch.double).clone()
>>> b = a * a
>>> Inplace.apply(a) # This would lead to wrong gradients!
>>> # but the engine would not know unless we mark_dirty
>>> b.backward() # RuntimeError: one of the variables needed for gradient
>>> # computation has been modified by an inplace operation
```