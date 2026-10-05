# torch.Tensor.is_leaf

Tensor.is_leaf

All Tensors that have [`requires_grad`](torch.Tensor.requires_grad.html#torch.Tensor.requires_grad) which is `False` will be leaf Tensors by convention.

For Tensors that have [`requires_grad`](torch.Tensor.requires_grad.html#torch.Tensor.requires_grad) which is `True`, they will be leaf Tensors if they were
created by the user. This means that they are not the result of an operation and so
`grad_fn` is None.

Only leaf Tensors will have their [`grad`](torch.Tensor.grad.html#torch.Tensor.grad) populated during a call to [`backward()`](torch.Tensor.backward.html#torch.Tensor.backward).
To get [`grad`](torch.Tensor.grad.html#torch.Tensor.grad) populated for non-leaf Tensors, you can use [`retain_grad()`](torch.Tensor.retain_grad.html#torch.Tensor.retain_grad).

Example:

```
>>> a = torch.rand(10, requires_grad=True)
>>> a.is_leaf
True
>>> b = torch.rand(10, requires_grad=True).cuda()
>>> b.is_leaf
False
# b was created by the operation that cast a cpu Tensor into a cuda Tensor
>>> c = torch.rand(10, requires_grad=True) + 2
>>> c.is_leaf
False
# c was created by the addition operation
>>> d = torch.rand(10).cuda()
>>> d.is_leaf
True
# d does not require gradients and so has no operation creating it (that is tracked by the autograd engine)
>>> e = torch.rand(10).cuda().requires_grad_()
>>> e.is_leaf
True
# e requires gradients and has no operations creating it
>>> f = torch.rand(10, requires_grad=True, device="cuda")
>>> f.is_leaf
True
# f requires grad, has no operation creating it
```