# AdaptiveMaxPool3d

*class*torch.nn.AdaptiveMaxPool3d(*output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/b896199bee9ca0e125f6ec366a265418a8f3290e/torch/nn/modules/pooling.py#L1440)

Applies a 3D adaptive max pooling over an input signal composed of several input planes.

The output is of size Dout×Hout×WoutD_{out} \times H_{out} \times W_{out}Dout​×Hout​×Wout​, for any input size.
The number of output features is equal to the number of input planes.

Each output element is the maximum over a cuboidal region of the input. The bounds
are computed independently for each spatial dimension, from an output index
kkk, an input size III and an output size OOO:

start(k,I,O)=⌊k×IO⌋end(k,I,O)=⌈(k+1)×IO⌉\text{start}(k, I, O) = \left\lfloor \frac{k \times I}{O} \right\rfloor
\qquad
\text{end}(k, I, O) = \left\lceil \frac{(k + 1) \times I}{O} \right\rceil

start(k,I,O)=⌊Ok×I​⌋end(k,I,O)=⌈O(k+1)×I​⌉

The region for output element (d,h,w)(d, h, w)(d,h,w) spans
[start(d,Din,Dout),end(d,Din,Dout))[\text{start}(d, D_{in}, D_{out}), \text{end}(d, D_{in}, D_{out}))[start(d,Din​,Dout​),end(d,Din​,Dout​)) along the
depth dimension, and likewise with (Hin,Hout)(H_{in}, H_{out})(Hin​,Hout​) and
(Win,Wout)(W_{in}, W_{out})(Win​,Wout​) along height and width.

When an input size is not divisible by the corresponding output size, these regions
may have different sizes and may overlap.

Parameters:

- **output_size** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*|**None**|*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*|**None**,*[*int*](https://docs.python.org/3/builtins/functions.html#int)*|**None**,*[*int*](https://docs.python.org/3/builtins/functions.html#int)*|**None**]*) - the target output size of the image of the form Dout×Hout×WoutD_{out} \times H_{out} \times W_{out}Dout​×Hout​×Wout​.
Can be a tuple (Dout,Hout,Wout)(D_{out}, H_{out}, W_{out})(Dout​,Hout​,Wout​) or a single
DoutD_{out}Dout​ for a cube Dout×Dout×DoutD_{out} \times D_{out} \times D_{out}Dout​×Dout​×Dout​.
DoutD_{out}Dout​, HoutH_{out}Hout​ and WoutW_{out}Wout​ can be either an
`int`, or `None` which means the size will be the same as that of the input.
- **return_indices** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - if `True`, will return the indices along with the outputs.
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

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/b896199bee9ca0e125f6ec366a265418a8f3290e/torch/nn/modules/pooling.py#L1496)

Runs the forward pass.