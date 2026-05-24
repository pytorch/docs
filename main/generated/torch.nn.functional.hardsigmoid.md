# torch.nn.functional.hardsigmoid

torch.nn.functional.hardsigmoid(*input*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/15e96b281415c58d3acf5d63d86df9d68744ee16/torch/nn/functional.py#L2312)

Apply the Hardsigmoid function element-wise.

Hardsigmoid(x)={0if x≤−3,1if x≥+3,x/6+1/2otherwise\text{Hardsigmoid}(x) = \begin{cases}
 0 & \text{if~} x \le -3, \\
 1 & \text{if~} x \ge +3, \\
 x / 6 + 1 / 2 & \text{otherwise}
\end{cases}

Hardsigmoid(x)=⎩⎨⎧​01x/6+1/2​if x≤−3,if x≥+3,otherwise​
Parameters:

**inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to `True`, will do this operation in-place. Default: `False`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

See [`Hardsigmoid`](torch.nn.Hardsigmoid.html#torch.nn.Hardsigmoid) for more details.