# torch.set_flush_denormal

torch.set_flush_denormal(*mode*) → [bool](https://docs.python.org/3/library/functions.html#bool)

Disables denormal floating numbers on CPU.

Returns `True` if your system supports flushing denormal numbers and it
successfully configures flush denormal mode. `set_flush_denormal()`
is supported on x86 architectures supporting SSE3 and AArch64 architecture.

Parameters:

**mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Controls whether to enable flush denormal mode or not

Example:

```
>>> torch.set_flush_denormal(True)
True
>>> torch.tensor([1e-323], dtype=torch.float64)
tensor([ 0.], dtype=torch.float64)
>>> torch.set_flush_denormal(False)
True
>>> torch.tensor([1e-323], dtype=torch.float64)
tensor(9.88131e-324 *
 [ 1.0000], dtype=torch.float64)
```