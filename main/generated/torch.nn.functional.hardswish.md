# torch.nn.functional.hardswish

torch.nn.functional.hardswish(*input*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/nn/functional.py#L2426)

Apply hardswish function, element-wise.

Follows implementation as described in the paper:
[Searching for MobileNetV3](https://arxiv.org/abs/1905.02244).

Hardswish(x)={0if x≤−3,xif x≥+3,x⋅(x+3)/6otherwise\text{Hardswish}(x) = \begin{cases}
 0 & \text{if~} x \le -3, \\
 x & \text{if~} x \ge +3, \\
 x \cdot (x + 3) /6 & \text{otherwise}
\end{cases}

Hardswish(x)=⎩⎨⎧​0xx⋅(x+3)/6​if x≤−3,if x≥+3,otherwise​

See [`Hardswish`](torch.nn.Hardswish.html#torch.nn.Hardswish) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)