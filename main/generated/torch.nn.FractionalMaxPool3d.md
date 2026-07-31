# FractionalMaxPool3d

*class*torch.nn.FractionalMaxPool3d(*kernel_size*, *output_size=None*, *output_ratio=None*, *return_indices=False*, *_random_samples=None*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/nn/modules/pooling.py#L1002)

Applies a 3D fractional max pooling over an input signal composed of several input planes.

Fractional MaxPooling is described in detail in the paper [Fractional MaxPooling](https://arxiv.org/abs/1412.6071) by Ben Graham

The max-pooling operation is applied in kT×kH×kWkT \times kH \times kWkT×kH×kW regions by a stochastic
step size determined by the target output size.
The number of output features is equal to the number of input planes.

Note

Exactly one of `output_size` or `output_ratio` must be defined.

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the size of the window to take a max over.
Can be a single number k (for a square kernel of k x k x k) or a tuple (kt x kh x kw),
k must be greater than 0.
- **output_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the target output size of the image of the form oT x oH x oW.
Can be a tuple (oT, oH, oW) or a single number oH for a square image oH x oH x oH
- **output_ratio** ([*float*](https://docs.python.org/3/library/functions.html#float)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*float*](https://docs.python.org/3/library/functions.html#float)*,*[*float*](https://docs.python.org/3/library/functions.html#float)*,*[*float*](https://docs.python.org/3/library/functions.html#float)*]*) - If one wants to have an output size as a ratio of the input size, this option can be given.
This has to be a number or tuple in the range (0, 1)
- **return_indices** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, will return the indices along with the outputs.
Useful to pass to `nn.MaxUnpool3d()`. Default: `False`

Shape:

- Input: (N,C,Tin,Hin,Win)(N, C, T_{in}, H_{in}, W_{in})(N,C,Tin​,Hin​,Win​) or (C,Tin,Hin,Win)(C, T_{in}, H_{in}, W_{in})(C,Tin​,Hin​,Win​).
- Output: (N,C,Tout,Hout,Wout)(N, C, T_{out}, H_{out}, W_{out})(N,C,Tout​,Hout​,Wout​) or (C,Tout,Hout,Wout)(C, T_{out}, H_{out}, W_{out})(C,Tout​,Hout​,Wout​), where
(Tout,Hout,Wout)=output_size(T_{out}, H_{out}, W_{out})=\text{output\_size}(Tout​,Hout​,Wout​)=output_size or
(Tout,Hout,Wout)=output_ratio×(Tin,Hin,Win)(T_{out}, H_{out}, W_{out})=\text{output\_ratio} \times (T_{in}, H_{in}, W_{in})(Tout​,Hout​,Wout​)=output_ratio×(Tin​,Hin​,Win​)

Examples

```
>>> # pool of cubic window of size=3, and target output size 13x12x11
>>> m = nn.FractionalMaxPool3d(3, output_size=(13, 12, 11))
>>> # pool of cubic window and target output size being half of input size
>>> m = nn.FractionalMaxPool3d(3, output_ratio=(0.5, 0.5, 0.5))
>>> input = torch.randn(20, 16, 50, 32, 16)
>>> output = m(input)
```