# torch.nn.functional.fractional_max_pool3d

torch.nn.functional.fractional_max_pool3d(*input*, *kernel_size*, *output_size=None*, *output_ratio=None*, *return_indices=False*, *_random_samples=None*)[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/_jit_internal.py#L627)

Applies 3D fractional max pooling over an input signal composed of several input planes.

Fractional MaxPooling is described in detail in the paper [Fractional MaxPooling](http://arxiv.org/abs/1412.6071) by Ben Graham

The max-pooling operation is applied in kT×kH×kWkT \times kH \times kWkT×kH×kW regions by a stochastic
step size determined by the target output size.
The number of output features is equal to the number of input planes.

Parameters:

- **kernel_size** - the size of the window to take a max over.
Can be a single number kkk (for a square kernel of k×k×kk \times k \times kk×k×k)
or a tuple (kT, kH, kW)
- **output_size** - the target output size of the form oT×oH×oWoT \times oH \times oWoT×oH×oW.
Can be a tuple (oT, oH, oW) or a single number oHoHoH for a cubic output
oH×oH×oHoH \times oH \times oHoH×oH×oH
- **output_ratio** - If one wants to have an output size as a ratio of the input size, this option can be given.
This has to be a number or tuple in the range (0, 1)
- **return_indices** - if `True`, will return the indices along with the outputs.
Useful to pass to [`max_unpool3d()`](torch.nn.functional.max_unpool3d.html#torch.nn.functional.max_unpool3d).

Shape:

- Input: (N,C,Tin,Hin,Win)(N, C, T_{in}, H_{in}, W_{in})(N,C,Tin​,Hin​,Win​) or (C,Tin,Hin,Win)(C, T_{in}, H_{in}, W_{in})(C,Tin​,Hin​,Win​).
- Output: (N,C,Tout,Hout,Wout)(N, C, T_{out}, H_{out}, W_{out})(N,C,Tout​,Hout​,Wout​) or (C,Tout,Hout,Wout)(C, T_{out}, H_{out}, W_{out})(C,Tout​,Hout​,Wout​), where
(Tout,Hout,Wout)=output_size(T_{out}, H_{out}, W_{out})=\text{output\_size}(Tout​,Hout​,Wout​)=output_size or
(Tout,Hout,Wout)=output_ratio×(Tin,Hin,Win)(T_{out}, H_{out}, W_{out})=\text{output\_ratio} \times (T_{in}, H_{in}, W_{in})(Tout​,Hout​,Wout​)=output_ratio×(Tin​,Hin​,Win​)

Examples::

```
>>> input = torch.randn(20, 16, 50, 32, 16)
>>> # pool of cubic window of size=3, and target output size 13x12x11
>>> F.fractional_max_pool3d(input, 3, output_size=(13, 12, 11))
>>> # pool of cubic window and target output size being half of input size
>>> F.fractional_max_pool3d(input, 3, output_ratio=(0.5, 0.5, 0.5))
```