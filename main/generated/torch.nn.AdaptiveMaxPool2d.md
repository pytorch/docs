# AdaptiveMaxPool2d

*class*torch.nn.AdaptiveMaxPool2d(*output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/nn/modules/pooling.py#L1348)

Applies a 2D adaptive max pooling over an input signal composed of several input planes.

The output is of size Hout×WoutH_{out} \times W_{out}Hout​×Wout​, for any input size.
The number of output features is equal to the number of input planes.

Parameters:

- **output_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None**|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*|**None**,*[*int*](https://docs.python.org/3/library/functions.html#int)*|**None**]*) - the target output size of the image of the form Hout×WoutH_{out} \times W_{out}Hout​×Wout​.
Can be a tuple (Hout,Wout)(H_{out}, W_{out})(Hout​,Wout​) or a single HoutH_{out}Hout​ for a
square image Hout×HoutH_{out} \times H_{out}Hout​×Hout​. HoutH_{out}Hout​ and WoutW_{out}Wout​
can be either a `int`, or `None` which means the size will be the same as that
of the input.
- **return_indices** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, will return the indices along with the outputs.
Useful to pass to nn.MaxUnpool2d. Default: `False`

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H_{in}, W_{in})(C,Hin​,Win​).
- Output: (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) or (C,Hout,Wout)(C, H_{out}, W_{out})(C,Hout​,Wout​), where
(Hout,Wout)=output_size(H_{out}, W_{out})=\text{output\_size}(Hout​,Wout​)=output_size.

Examples

```
>>> # target output size of 5x7
>>> m = nn.AdaptiveMaxPool2d((5, 7))
>>> input = torch.randn(1, 64, 8, 9)
>>> output = m(input)
>>> # target output size of 7x7 (square)
>>> m = nn.AdaptiveMaxPool2d(7)
>>> input = torch.randn(1, 64, 10, 9)
>>> output = m(input)
>>> # target output size of 10x7
>>> m = nn.AdaptiveMaxPool2d((None, 7))
>>> input = torch.randn(1, 64, 10, 9)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/nn/modules/pooling.py#L1386)

Runs the forward pass.