# torch.bucketize

torch.bucketize(*input*, *boundaries*, ***, *out_int32=False*, *right=False*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns the indices of the buckets to which each value in the `input` belongs, where the
boundaries of the buckets are set by `boundaries`. Return a new tensor with the same size
as `input`. If `right` is False (default), then the left boundary is open. Note that
this behavior is opposite the behavior of
[numpy.digitize](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html).
More formally, the returned index satisfies the following rules:

| `right` | *returned index satisfies* |
| --- | --- |
| False | `boundaries[i-1] < input[m][n]...[l][x] <= boundaries[i]` |
| True | `boundaries[i-1] <= input[m][n]...[l][x] < boundaries[i]` |

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)*or**Scalar*) - N-D tensor or a Scalar containing the search value(s).
- **boundaries** ([*Tensor*](../tensors.html#torch.Tensor)) - 1-D tensor, must contain a strictly increasing sequence, or the return value is undefined.

Keyword Arguments:

- **out_int32** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - indicate the output data type. torch.int32 if True, torch.int64 otherwise.
Default value is False, i.e. default output data type is torch.int64.
- **right** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - determines the behavior for values in `boundaries`. See the table above.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor, must be the same size as `input` if provided.

Example:

```
>>> boundaries = torch.tensor([1, 3, 5, 7, 9])
>>> boundaries
tensor([1, 3, 5, 7, 9])
>>> v = torch.tensor([[3, 6, 9], [3, 6, 9]])
>>> v
tensor([[3, 6, 9],
 [3, 6, 9]])
>>> torch.bucketize(v, boundaries)
tensor([[1, 3, 4],
 [1, 3, 4]])
>>> torch.bucketize(v, boundaries, right=True)
tensor([[2, 3, 5],
 [2, 3, 5]])
```