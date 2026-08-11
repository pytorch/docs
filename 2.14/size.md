# torch.Size

`torch.Size` is the result type of a call to [`torch.Tensor.size()`](generated/torch.Tensor.size.html#torch.Tensor.size). It describes the size of all dimensions
of the original tensor. As a subclass of [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple), it supports common sequence operations like indexing and
length.

Example:

```
>>> x = torch.ones(10, 20, 30)
 >>> s = x.size()
 >>> s
 torch.Size([10, 20, 30])
 >>> s[1]
 20
 >>> len(s)
 3
```

*class*torch.Size(*iterable=()*, */*)

count(*value*, */*)

Return number of occurrences of value.

index(*value*, *start=0*, *stop=9223372036854775807*, */*)

Return first index of value.

Raises ValueError if the value is not present.

numel() → [int](https://docs.python.org/3/library/functions.html#int)

Returns the number of elements a [`torch.Tensor`](tensors.html#torch.Tensor) with the given size would contain.

More formally, for a tensor `x = tensor.ones(10, 10)` with size `s = torch.Size([10, 10])`,
`x.numel() == x.size().numel() == s.numel() == 100` holds true.

Example:

```
>>> x=torch.ones(10, 10)
>>> s=x.size()
>>> s
torch.Size([10, 10])
>>> s.numel()
100
>>> x.numel() == s.numel()
True
```

Warning

This function does not return the number of dimensions described by `torch.Size`, but instead the number
of elements a [`torch.Tensor`](tensors.html#torch.Tensor) with that size would contain.