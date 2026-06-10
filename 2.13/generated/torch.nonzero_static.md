# torch.nonzero_static

torch.nonzero_static(*input*, ***, *size*, *fill_value=-1*) → [Tensor](../tensors.html#torch.Tensor)

Returns a 2-D tensor where each row is the index for a non-zero value.
The returned Tensor has the same torch.dtype as torch.nonzero().

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the size of non-zero elements expected to be included in the out
tensor. Pad the out tensor with fill_value if the size is larger
than total number of non-zero elements, truncate out tensor if size
is smaller. The size must be a non-negative integer.
- **fill_value** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the value to fill the output tensor with when size is larger
than the total number of non-zero elements. Default is -1 to represent
invalid index.

Example:

```
# Example 1: Padding
>>> input_tensor = torch.tensor([[1, 0], [3, 2]])
>>> static_size = 4
>>> t = torch.nonzero_static(input_tensor, size=static_size)
tensor([[ 0, 0],
 [ 1, 0],
 [ 1, 1],
 [ -1, -1]], dtype=torch.int64)

# Example 2: Truncating
>>> input_tensor = torch.tensor([[1, 0], [3, 2]])
>>> static_size = 2
>>> t = torch.nonzero_static(input_tensor, size=static_size)
tensor([[ 0, 0],
 [ 1, 0]], dtype=torch.int64)

# Example 3: 0 size
>>> input_tensor = torch.tensor([10])
>>> static_size = 0
>>> t = torch.nonzero_static(input_tensor, size=static_size)
tensor([], size=(0, 1), dtype=torch.int64)

# Example 4: 0 rank input
>>> input_tensor = torch.tensor(10)
>>> static_size = 2
>>> t = torch.nonzero_static(input_tensor, size=static_size)
tensor([], size=(2, 0), dtype=torch.int64)
```