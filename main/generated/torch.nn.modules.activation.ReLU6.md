# ReLU6

*class*torch.nn.modules.activation.ReLU6(*inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/modules/activation.py#L304)

Applies the ReLU6 function element-wise.

ReLU6(x)=min⁡(max⁡(0,x),6)\text{ReLU6}(x) = \min(\max(0,x), 6)

ReLU6(x)=min(max(0,x),6)
Parameters:

**inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - can optionally do the operation in-place. Default: `False`

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

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/modules/activation.py#L329)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)