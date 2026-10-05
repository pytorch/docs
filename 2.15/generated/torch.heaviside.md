# torch.heaviside

torch.heaviside(*input*, *values*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the Heaviside step function for each element in `input`.
The Heaviside step function is defined as:

heaviside(input,values)={0,if input < 0values,if input == 01,if input > 0\text{{heaviside}}(input, values) = \begin{cases}
 0, & \text{if input < 0}\\
 values, & \text{if input == 0}\\
 1, & \text{if input > 0}
\end{cases}

heaviside(input,values)=⎩⎨⎧​0,values,1,​if input < 0if input == 0if input > 0​
Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **values** ([*Tensor*](../tensors.html#torch.Tensor)) - The values to use where `input` is zero.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> input = torch.tensor([-1.5, 0, 2.0])
>>> values = torch.tensor([0.5])
>>> torch.heaviside(input, values)
tensor([0.0000, 0.5000, 1.0000])
>>> values = torch.tensor([1.2, -2.0, 3.5])
>>> torch.heaviside(input, values)
tensor([0., -2., 1.])
```