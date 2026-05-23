# AdaptiveMaxPool1d

*class*torch.nn.AdaptiveMaxPool1d(*output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/nn/modules/pooling.py#L1315)

Applies a 1D adaptive max pooling over an input signal composed of several input planes.

The output size is LoutL_{out}Lout​, for any input size.
The number of output features is equal to the number of input planes.

Parameters:

- **output_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the target output size LoutL_{out}Lout​.
- **return_indices** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, will return the indices along with the outputs.
Useful to pass to nn.MaxUnpool1d. Default: `False`

Shape:

- Input: (N,C,Lin)(N, C, L_{in})(N,C,Lin​) or (C,Lin)(C, L_{in})(C,Lin​).
- Output: (N,C,Lout)(N, C, L_{out})(N,C,Lout​) or (C,Lout)(C, L_{out})(C,Lout​), where
Lout=output_sizeL_{out}=\text{output\_size}Lout​=output_size.

Examples

```
>>> # target output size of 5
>>> m = nn.AdaptiveMaxPool1d(5)
>>> input = torch.randn(1, 64, 8)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/nn/modules/pooling.py#L1341)

Runs the forward pass.