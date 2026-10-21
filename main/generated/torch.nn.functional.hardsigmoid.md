# torch.nn.functional.hardsigmoid

torch.nn.functional.hardsigmoid(*input*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/7ffd47d270087d6dbafb876c0549d949aabf0a5a/torch/nn/functional.py#L2390)

Apply the Hardsigmoid function element-wise.

Hardsigmoid(x)={0if x≤−3,1if x≥+3,x/6+1/2otherwise\text{Hardsigmoid}(x) = \begin{cases}
 0 & \text{if~} x \le -3, \\
 1 & \text{if~} x \ge +3, \\
 x / 6 + 1 / 2 & \text{otherwise}
\end{cases}

Hardsigmoid(x)=⎩⎨⎧​01x/6+1/2​if x≤−3,if x≥+3,otherwise​
Parameters:

**inplace** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - If set to `True`, will do this operation in-place. Default: `False`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

See [`Hardsigmoid`](torch.nn.Hardsigmoid.html#torch.nn.Hardsigmoid) for more details.