# check_sparse_tensor_invariants

*class*torch.sparse.check_sparse_tensor_invariants(*enable=True*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/sparse/__init__.py#L453)

A tool to control checking sparse tensor invariants.

The following options exists to manage sparse tensor invariants
checking in sparse tensor construction:

1. Using a context manager:

```
with torch.sparse.check_sparse_tensor_invariants():
 run_my_model()
```
2. Using a procedural approach:

```
prev_checks_enabled = torch.sparse.check_sparse_tensor_invariants.is_enabled()
torch.sparse.check_sparse_tensor_invariants.enable()

run_my_model()

if not prev_checks_enabled:
 torch.sparse.check_sparse_tensor_invariants.disable()
```
3. Using function decoration:

```
@torch.sparse.check_sparse_tensor_invariants()
def run_my_model():
 ...

run_my_model()
```
4. Using `check_invariants` keyword argument in sparse tensor constructor call.
For example:

```
>>> torch.sparse_csr_tensor([0, 1, 3], [0, 1], [1, 2], check_invariants=True)
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
RuntimeError: `crow_indices[..., -1] == nnz` is not satisfied.
```

*static*disable()[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/sparse/__init__.py#L529)

Disable sparse tensor invariants checking in sparse tensor constructors.

See `torch.sparse.check_sparse_tensor_invariants.enable()` for more information.

*static*enable()[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/sparse/__init__.py#L509)

Enable sparse tensor invariants checking in sparse tensor constructors.

Note

By default, the sparse tensor invariants checks are disabled. Use
`torch.sparse.check_sparse_tensor_invariants.is_enabled()` to
retrieve the current state of sparse tensor invariants checking.

Note

The sparse tensor invariants check flag is effective to all sparse
tensor constructors, both in Python and ATen.

The flag can be locally overridden by the `check_invariants`
optional argument of the sparse tensor constructor functions.

*static*is_enabled()[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/sparse/__init__.py#L497)

Return True if the sparse tensor invariants checking is enabled.

Note

Use `torch.sparse.check_sparse_tensor_invariants.enable()` or
`torch.sparse.check_sparse_tensor_invariants.disable()` to
manage the state of the sparse tensor invariants checks.