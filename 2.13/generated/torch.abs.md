# torch.abs

torch.abs(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Computes the absolute value of each element in `input`.

outi=∣inputi∣\text{out}_{i} = |\text{input}_{i}|

outi​=∣inputi​∣
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.abs(torch.tensor([-1, -2, 3]))
tensor([ 1, 2, 3])
```