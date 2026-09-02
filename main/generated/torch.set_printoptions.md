# torch.set_printoptions

torch.set_printoptions(*precision=None*, *threshold=None*, *edgeitems=None*, *linewidth=None*, *profile=None*, *sci_mode=None*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/_tensor_str.py#L25)

Set options for printing. Items shamelessly taken from NumPy

Parameters:

- **precision** - Number of digits of precision for floating point output
(default = 4).
- **threshold** - Total number of array elements which trigger summarization
rather than full repr (default = 1000).
- **edgeitems** - Number of array items in summary at beginning and end of
each dimension (default = 3).
- **linewidth** - The number of characters per line for the purpose of
inserting line breaks (default = 80). Thresholded matrices will
ignore this parameter.
- **profile** - Sane defaults for pretty printing. Can override with any of
the above options. (any one of default, short, full)
- **sci_mode** - Enable (True) or disable (False) scientific notation. If
None (default) is specified, the value is defined by
torch._tensor_str._Formatter. This value is automatically chosen
by the framework.

Example:

```
>>> # Limit the precision of elements
>>> torch.set_printoptions(precision=2)
>>> torch.tensor([1.12345])
tensor([1.12])
>>> # Limit the number of elements shown
>>> torch.set_printoptions(threshold=5)
>>> torch.arange(10)
tensor([0, 1, 2, ..., 7, 8, 9])
>>> # Restore defaults
>>> torch.set_printoptions(profile='default')
>>> torch.tensor([1.12345])
tensor([1.1235])
>>> torch.arange(10)
tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```