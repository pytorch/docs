# ReLU6

*class*torch.ao.nn.quantized.ReLU6(*inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/2a8ba15825312e681c7dc6b12b79dec216aecd30/torch/ao/nn/quantized/modules/activation.py#L19)

Applies the element-wise function:

ReLU6(x)=min⁡(max⁡(x0,x),q(6))\text{ReLU6}(x) = \min(\max(x_0, x), q(6))ReLU6(x)=min(max(x0​,x),q(6)), where x0x_0x0​ is the
zero_point, and q(6)q(6)q(6) is the quantized representation of number 6.

Parameters:

**inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - can optionally do the operation in-place. Default: `False`

Shape:

- Input: (N,∗)(N, *)(N,∗) where * means, any number of additional
dimensions
- Output: (N,∗)(N, *)(N,∗), same shape as the input

![../_images/ReLU6.png](../_images/ReLU6.png)

Examples:

```
>>> m = nn.quantized.ReLU6()
>>> input = torch.randn(2)
>>> input = torch.quantize_per_tensor(input, 1.0, 0, dtype=torch.qint32)
>>> output = m(input)
```