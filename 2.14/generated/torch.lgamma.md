# torch.lgamma

torch.lgamma(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the natural logarithm of the absolute value of the gamma function on `input`.

outi=ln⁡∣Γ(inputi)∣\text{out}_{i} = \ln |\Gamma(\text{input}_{i})|

outi​=ln∣Γ(inputi​)∣
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.arange(0.5, 2, 0.5)
>>> torch.lgamma(a)
tensor([ 0.5724, 0.0000, -0.1208])
```