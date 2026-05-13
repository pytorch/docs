# torch.equal

torch.equal(*input*, *other*) → [bool](https://docs.python.org/3/library/functions.html#bool)

`True` if two tensors have the same size and elements, `False` otherwise.

Note

Tensors containing NaNs are never equal to each other. Additionally, this function does not
differentiate between the data types of the tensors during comparison. For more thorough tensor checks,
use [`torch.testing.assert_close()`](../testing.html#torch.testing.assert_close).

Example:

```
>>> torch.equal(torch.tensor([1, 2]), torch.tensor([1, 2]))
True
>>> torch.equal(torch.tensor([3, torch.nan]), torch.tensor([3, torch.nan]))
False
>>> torch.equal(torch.tensor([1, 2, 3], dtype=torch.int32), torch.tensor([1, 2, 3], dtype=torch.float32))
True
```