# torch.func.hessian

torch.func.hessian(*func*, *argnums=0*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/_functorch/eager_transforms.py#L1426)

Computes the Hessian of `func` with respect to the arg(s) at index
`argnum` via a forward-over-reverse strategy.

The forward-over-reverse strategy (composing `jacfwd(jacrev(func))`) is
a good default for good performance. It is possible to compute Hessians
through other compositions of [`jacfwd()`](torch.func.jacfwd.html#torch.func.jacfwd) and [`jacrev()`](torch.func.jacrev.html#torch.func.jacrev) like
`jacfwd(jacfwd(func))` or `jacrev(jacrev(func))`.

Parameters:

- **func** (*function*) - A Python function that takes one or more arguments,
one of which must be a Tensor, and returns one or more Tensors
- **argnums** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,**...**]*) - Optional, integer or tuple of integers,
saying which arguments to get the Hessian with respect to.
Default: 0.

Returns:

Returns a function that takes in the same inputs as `func` and
returns the Hessian of `func` with respect to the arg(s) at
`argnums`.

Return type:

Callable[..., Any]

Note

You may see this API error out with "forward-mode AD not implemented
for operator X". If so, please file a bug report and we will prioritize it.
An alternative is to use `jacrev(jacrev(func))`, which has better
operator coverage.

A basic usage with a R^N -> R^1 function gives a N x N Hessian:

```
>>> from torch.func import hessian
>>> def f(x):
>>> return x.sin().sum()
>>>
>>> x = torch.randn(5)
>>> hess = hessian(f)(x) # equivalent to jacfwd(jacrev(f))(x)
>>> assert torch.allclose(hess, torch.diag(-x.sin()))
```