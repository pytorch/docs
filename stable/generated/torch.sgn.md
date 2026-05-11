# torch.sgn

torch.sgn(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

This function is an extension of torch.sign() to complex tensors.
It computes a new tensor whose elements have
the same angles as the corresponding elements of `input` and
absolute values (i.e. magnitudes) of one for complex tensors and
is equivalent to torch.sign() for non-complex tensors.

outi={0∣inputi∣==0inputi∣inputi∣otherwise\text{out}_{i} = \begin{cases}
 0 & |\text{{input}}_i| == 0 \\
 \frac{{\text{{input}}_i}}{|{\text{{input}}_i}|} & \text{otherwise}
 \end{cases}

outi​={0∣inputi​∣inputi​​​∣inputi​∣==0otherwise​
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> t = torch.tensor([3+4j, 7-24j, 0, 1+2j])
>>> t.sgn()
tensor([0.6000+0.8000j, 0.2800-0.9600j, 0.0000+0.0000j, 0.4472+0.8944j])
```