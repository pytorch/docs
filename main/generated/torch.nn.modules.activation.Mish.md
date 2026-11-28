# Mish

*class*torch.nn.modules.activation.Mish(*inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/nn/modules/activation.py#L489)

Applies the Mish function, element-wise.

Mish: A Self Regularized Non-Monotonic Neural Activation Function.

Mish(x)=x∗Tanh(Softplus(x))\text{Mish}(x) = x * \text{Tanh}(\text{Softplus}(x))

Mish(x)=x∗Tanh(Softplus(x))

Note

See [Mish: A Self Regularized Non-Monotonic Neural Activation Function](https://arxiv.org/abs/1908.08681)

Shape:

- Input: (∗)(*)(∗), where ∗*∗ means any number of dimensions.
- Output: (∗)(*)(∗), same shape as the input.

![../_images/Mish.png](../_images/Mish.png)

Examples:

```
>>> m = nn.Mish()
>>> input = torch.randn(2)
>>> output = m(input)
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/nn/modules/activation.py#L526)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/nn/modules/activation.py#L520)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)