# LocalResponseNorm

*class*torch.nn.modules.normalization.LocalResponseNorm(*size*, *alpha=0.0001*, *beta=0.75*, *k=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/nn/modules/normalization.py#L16)

Applies local response normalization over an input signal.

The input signal is composed of several input planes, where channels occupy the second dimension.
Applies normalization across channels.

bc=ac(k+αn∑c′=max⁡(0,c−n/2)min⁡(N−1,c+n/2)ac′2)−βb_{c} = a_{c}\left(k + \frac{\alpha}{n}
\sum_{c'=\max(0, c-n/2)}^{\min(N-1,c+n/2)}a_{c'}^2\right)^{-\beta}

bc​=ac​​k+nα​c′=max(0,c−n/2)∑min(N−1,c+n/2)​ac′2​​−β
Parameters:

- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - amount of neighbouring channels used for normalization
- **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) - multiplicative factor. Default: 0.0001
- **beta** ([*float*](https://docs.python.org/3/library/functions.html#float)) - exponent. Default: 0.75
- **k** ([*float*](https://docs.python.org/3/library/functions.html#float)) - additive factor. Default: 1

Shape:

- Input: (N,C,∗)(N, C, *)(N,C,∗)
- Output: (N,C,∗)(N, C, *)(N,C,∗) (same shape as input)

Examples:

```
>>> lrn = nn.LocalResponseNorm(2)
>>> signal_2d = torch.randn(32, 5, 24, 24)
>>> signal_4d = torch.randn(16, 5, 7, 7, 7, 7)
>>> output_2d = lrn(signal_2d)
>>> output_4d = lrn(signal_4d)
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/nn/modules/normalization.py#L67)

Return the extra representation of the module.

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/nn/modules/normalization.py#L61)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)