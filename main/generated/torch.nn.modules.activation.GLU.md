# GLU

*class*torch.nn.modules.activation.GLU(*dim=-1*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/nn/modules/activation.py#L737)

Applies the gated linear unit function.

GLU(a,b)=a⊗σ(b){GLU}(a, b)= a \otimes \sigma(b)GLU(a,b)=a⊗σ(b) where aaa is the first half
of the input matrices and bbb is the second half.

Parameters:

**dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the dimension on which to split the input. Default: -1

Shape:

- Input: (∗1,N,∗2)(\ast_1, N, \ast_2)(∗1​,N,∗2​) where * means, any number of additional
dimensions
- Output: (∗1,M,∗2)(\ast_1, M, \ast_2)(∗1​,M,∗2​) where M=N/2M=N/2M=N/2

Examples:

```
>>> m = nn.GLU()
>>> input = torch.randn(4, 2)
>>> output = m(input)
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/nn/modules/activation.py#L771)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/nn/modules/activation.py#L765)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)