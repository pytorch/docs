# torch.Tensor.numpy

Tensor.numpy(***, *force=False*) → [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)

Returns the tensor as a NumPy `ndarray`.

If `force` is `False` (the default), the conversion
is performed only if the tensor is on the CPU, does not require grad,
does not have its conjugate bit set, and is a dtype and layout that
NumPy supports. The returned ndarray and the tensor will share their
storage, so changes to the tensor will be reflected in the ndarray
and vice versa.

If `force` is `True` this is equivalent to
calling `t.detach().cpu().resolve_conj().resolve_neg().numpy()`.
If the tensor isn't on the CPU or the conjugate or negative bit is set,
the tensor won't share its storage with the returned ndarray.
Setting `force` to `True` can be a useful shorthand.

Parameters:

**force** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, the ndarray may be a copy of the tensor
instead of always sharing memory, defaults to `False`.