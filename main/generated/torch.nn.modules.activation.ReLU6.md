# ReLU6

*class*torch.nn.modules.activation.ReLU6(*inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/b7954b2399da4803024b9a2850e39c588522015f/torch/nn/modules/activation.py#L304)

Applies the ReLU6 function element-wise.

ReLU6(x)=min⁡(max⁡(0,x),6)\text{ReLU6}(x) = \min(\max(0,x), 6)

ReLU6(x)=min(max(0,x),6)
Parameters:

**inplace** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - can optionally do the operation in-place. Default: `False`

Shape:

- Input: (∗)(*)(∗), where ∗*∗ means any number of dimensions.
- Output: (∗)(*)(∗), same shape as the input.

![../_images/ReLU6.png](../_images/ReLU6.png)

Examples:

```
>>> m = nn.ReLU6()
>>> input = torch.randn(2)
>>> output = m(input)
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/b7954b2399da4803024b9a2850e39c588522015f/torch/nn/modules/activation.py#L329)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)