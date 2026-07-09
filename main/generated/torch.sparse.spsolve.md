# torch.sparse.spsolve

torch.sparse.spsolve(*input*, *other*, ***, *left=True*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/7a37a01092627acd59ddfcb9cefe5a578f5f6996/torch/sparse/__init__.py#L317)

Computes the solution of a square system of linear equations with
a unique solution. Its purpose is similar to [`torch.linalg.solve()`](torch.linalg.solve.html#torch.linalg.solve),
except that the system is defined by a sparse CSR matrix with layout
sparse_csr.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - a sparse CSR matrix of shape (n, n) representing the
coefficients of the linear system.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - a dense matrix of shape (n, ) representing the right-hand
side of the linear system.
- **left** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to solve the system for input @ out = other
(default) or out @ input = other. Only left=True is supported.