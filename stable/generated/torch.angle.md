# torch.angle

torch.angle(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Computes the element-wise angle (in radians) of the given `input` tensor.

outi=angle(inputi)\text{out}_{i} = angle(\text{input}_{i})

outi​=angle(inputi​)
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Note

Starting in PyTorch 1.8, angle returns pi for negative real numbers,
zero for non-negative real numbers, and propagates NaNs. Previously
the function would return zero for all real numbers and not propagate
floating-point NaNs.

Example:

```
>>> torch.angle(torch.tensor([-1 + 1j, -2 + 2j, 3 - 3j]))*180/3.14159
tensor([ 135., 135, -45])
```