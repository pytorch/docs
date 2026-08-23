# torch.func.grad_and_value

torch.func.grad_and_value(*func*, *argnums=0*, *has_aux=False*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/_functorch/apis.py#L468)

Returns a function to compute a tuple of the gradient and primal, or
forward, computation.

Parameters:

- **func** (*Callable*) - A Python function that takes one or more arguments.
Must return a single-element Tensor. If specified `has_aux`
equals `True`, function can return a tuple of single-element
Tensor and other auxiliary objects: `(output, aux)`.
- **argnums** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - Specifies arguments to compute gradients
with respect to. `argnums` can be single integer or tuple of
integers. Default: 0.
- **has_aux** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Flag indicating that `func` returns a tensor and
other auxiliary objects: `(output, aux)`. Default: False.

Returns:

Function to compute a tuple of gradients with respect to its inputs
and the forward computation. By default, the output of the function is
a tuple of the gradient tensor(s) with respect to the first argument
and the primal computation. If specified `has_aux` equals
`True`, tuple of gradients and tuple of the forward computation with
output auxiliary objects is returned. If `argnums` is a tuple of
integers, a tuple of a tuple of the output gradients with respect to
each `argnums` value and the forward computation is returned.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]]

See [`grad()`](torch.func.grad.html#torch.func.grad) for examples