# torch.is_nonzero

torch.is_nonzero(*input*)

Returns True if the `input` is a single element tensor which is not equal to zero
after type conversions.
i.e. not equal to `torch.tensor([0.])` or `torch.tensor([0])` or
`torch.tensor([False])`.
Throws a `RuntimeError` if `torch.numel() != 1` (even in case
of sparse tensors).

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Examples:

```
>>> torch.is_nonzero(torch.tensor([0.]))
False
>>> torch.is_nonzero(torch.tensor([1.5]))
True
>>> torch.is_nonzero(torch.tensor([False]))
False
>>> torch.is_nonzero(torch.tensor([3]))
True
>>> torch.is_nonzero(torch.tensor([1, 3, 5]))
Traceback (most recent call last):
...
RuntimeError: Boolean value of Tensor with more than one value is ambiguous
>>> torch.is_nonzero(torch.tensor([]))
Traceback (most recent call last):
...
RuntimeError: Boolean value of Tensor with no values is ambiguous
```