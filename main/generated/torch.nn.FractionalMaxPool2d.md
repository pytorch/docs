# FractionalMaxPool2d

*class*torch.nn.FractionalMaxPool2d(*kernel_size*, *output_size=None*, *output_ratio=None*, *return_indices=False*, *_random_samples=None*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/nn/modules/pooling.py#L913)

Applies a 2D fractional max pooling over an input signal composed of several input planes.

Fractional MaxPooling is described in detail in the paper [Fractional MaxPooling](https://arxiv.org/abs/1412.6071) by Ben Graham

The max-pooling operation is applied in kH×kWkH \times kWkH×kW regions by a stochastic
step size determined by the target output size.
The number of output features is equal to the number of input planes.

Note

Exactly one of `output_size` or `output_ratio` must be defined.

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the size of the window to take a max over.
Can be a single number k (for a square kernel of k x k) or a tuple (kh, kw)
- **output_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the target output size of the image of the form oH x oW.
Can be a tuple (oH, oW) or a single number oH for a square image oH x oH.
Note that we must have kH+oH−1<=HinkH + oH - 1 <= H_{in}kH+oH−1<=Hin​ and kW+oW−1<=WinkW + oW - 1 <= W_{in}kW+oW−1<=Win​
- **output_ratio** ([*float*](https://docs.python.org/3/library/functions.html#float)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*float*](https://docs.python.org/3/library/functions.html#float)*,*[*float*](https://docs.python.org/3/library/functions.html#float)*]*) - If one wants to have an output size as a ratio of the input size, this option can be given.
This has to be a number or tuple in the range (0, 1).
Note that we must have kH+(output_ratio_H∗Hin)−1<=HinkH + (output\_ratio\_H * H_{in}) - 1 <= H_{in}kH+(output_ratio_H∗Hin​)−1<=Hin​
and kW+(output_ratio_W∗Win)−1<=WinkW + (output\_ratio\_W * W_{in}) - 1 <= W_{in}kW+(output_ratio_W∗Win​)−1<=Win​
- **return_indices** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, will return the indices along with the outputs.
Useful to pass to `nn.MaxUnpool2d()`. Default: `False`

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H_{in}, W_{in})(C,Hin​,Win​).
- Output: (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) or (C,Hout,Wout)(C, H_{out}, W_{out})(C,Hout​,Wout​), where
(Hout,Wout)=output_size(H_{out}, W_{out})=\text{output\_size}(Hout​,Wout​)=output_size or
(Hout,Wout)=output_ratio×(Hin,Win)(H_{out}, W_{out})=\text{output\_ratio} \times (H_{in}, W_{in})(Hout​,Wout​)=output_ratio×(Hin​,Win​).

Examples

```
>>> # pool of square window of size=3, and target output size 13x12
>>> m = nn.FractionalMaxPool2d(3, output_size=(13, 12))
>>> # pool of square window and target output size being half of input image size
>>> m = nn.FractionalMaxPool2d(3, output_ratio=(0.5, 0.5))
>>> input = torch.randn(20, 16, 50, 32)
>>> output = m(input)
```