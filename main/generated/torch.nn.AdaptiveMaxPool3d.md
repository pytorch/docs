# AdaptiveMaxPool3d

*class*torch.nn.AdaptiveMaxPool3d(*output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/modules/pooling.py#L1389)

Applies a 3D adaptive max pooling over an input signal composed of several input planes.

The output is of size Dout×Hout×WoutD_{out} \times H_{out} \times W_{out}Dout​×Hout​×Wout​, for any input size.
The number of output features is equal to the number of input planes.

Parameters:

- **output_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None**|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*|**None**,*[*int*](https://docs.python.org/3/library/functions.html#int)*|**None**,*[*int*](https://docs.python.org/3/library/functions.html#int)*|**None**]*) - the target output size of the image of the form Dout×Hout×WoutD_{out} \times H_{out} \times W_{out}Dout​×Hout​×Wout​.
Can be a tuple (Dout,Hout,Wout)(D_{out}, H_{out}, W_{out})(Dout​,Hout​,Wout​) or a single
DoutD_{out}Dout​ for a cube Dout×Dout×DoutD_{out} \times D_{out} \times D_{out}Dout​×Dout​×Dout​.
DoutD_{out}Dout​, HoutH_{out}Hout​ and WoutW_{out}Wout​ can be either a
`int`, or `None` which means the size will be the same as that of the input.
- **return_indices** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, will return the indices along with the outputs.
Useful to pass to nn.MaxUnpool3d. Default: `False`

Shape:

- Input: (N,C,Din,Hin,Win)(N, C, D_{in}, H_{in}, W_{in})(N,C,Din​,Hin​,Win​) or (C,Din,Hin,Win)(C, D_{in}, H_{in}, W_{in})(C,Din​,Hin​,Win​).
- Output: (N,C,Dout,Hout,Wout)(N, C, D_{out}, H_{out}, W_{out})(N,C,Dout​,Hout​,Wout​) or (C,Dout,Hout,Wout)(C, D_{out}, H_{out}, W_{out})(C,Dout​,Hout​,Wout​),
where (Dout,Hout,Wout)=output_size(D_{out}, H_{out}, W_{out})=\text{output\_size}(Dout​,Hout​,Wout​)=output_size.

Examples

```
>>> # target output size of 5x7x9
>>> m = nn.AdaptiveMaxPool3d((5, 7, 9))
>>> input = torch.randn(1, 64, 8, 9, 10)
>>> output = m(input)
>>> # target output size of 7x7x7 (cube)
>>> m = nn.AdaptiveMaxPool3d(7)
>>> input = torch.randn(1, 64, 10, 9, 8)
>>> output = m(input)
>>> # target output size of 7x9x8
>>> m = nn.AdaptiveMaxPool3d((7, None, None))
>>> input = torch.randn(1, 64, 10, 9, 8)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/modules/pooling.py#L1428)

Runs the forward pass.