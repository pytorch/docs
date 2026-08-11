# torch.exp

torch.exp(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the exponential of the elements
of the input tensor `input`.

yi=exiy_{i} = e^{x_{i}}

yi​=exi​
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.exp(torch.tensor([0, math.log(2.)]))
tensor([ 1., 2.])
```