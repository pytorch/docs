# AdaptiveMaxPool2d

*class*torch.nn.modules.pooling.AdaptiveMaxPool2d(*output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/nn/modules/pooling.py#L1375)

Applies a 2D adaptive max pooling over an input signal composed of several input planes.

The output is of size Hout×WoutH_{out} \times W_{out}Hout​×Wout​, for any input size.
The number of output features is equal to the number of input planes.

Each output element is the maximum over a rectangular region of the input. The
bounds are computed independently for each spatial dimension, from an output index
kkk, an input size III and an output size OOO:

start(k,I,O)=⌊k×IO⌋end(k,I,O)=⌈(k+1)×IO⌉\text{start}(k, I, O) = \left\lfloor \frac{k \times I}{O} \right\rfloor
\qquad
\text{end}(k, I, O) = \left\lceil \frac{(k + 1) \times I}{O} \right\rceil

start(k,I,O)=⌊Ok×I​⌋end(k,I,O)=⌈O(k+1)×I​⌉

Writing h0=start(h,Hin,Hout)h_0 = \text{start}(h, H_{in}, H_{out})h0​=start(h,Hin​,Hout​) and
h1=end(h,Hin,Hout)h_1 = \text{end}(h, H_{in}, H_{out})h1​=end(h,Hin​,Hout​), and likewise w0w_0w0​ and
w1w_1w1​ from (Win,Wout)(W_{in}, W_{out})(Win​,Wout​), the output is

out(Ni,Cj,h,w)=max⁡h0≤m<h1max⁡w0≤n<w1input(Ni,Cj,m,n)out(N_i, C_j, h, w) = \max_{h_0 \le m < h_1} \max_{w_0 \le n < w_1}
 input(N_i, C_j, m, n)

out(Ni​,Cj​,h,w)=h0​≤m<h1​max​w0​≤n<w1​max​input(Ni​,Cj​,m,n)

When an input size is not divisible by the corresponding output size, these regions
may have different sizes and may overlap. For example, a 3×33 \times 33×3 input
pooled to 2×22 \times 22×2 takes the maximum over four overlapping
2×22 \times 22×2 regions.

Parameters:

- **output_size** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*|**None**|*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*|**None**,*[*int*](https://docs.python.org/3/builtins/functions.html#int)*|**None**]*) - the target output size of the image of the form Hout×WoutH_{out} \times W_{out}Hout​×Wout​.
Can be a tuple (Hout,Wout)(H_{out}, W_{out})(Hout​,Wout​) or a single HoutH_{out}Hout​ for a
square image Hout×HoutH_{out} \times H_{out}Hout​×Hout​. HoutH_{out}Hout​ and WoutW_{out}Wout​
can be either an `int`, or `None` which means the size will be the same as that
of the input.
- **return_indices** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - if `True`, will return the indices along with the outputs.
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

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/nn/modules/pooling.py#L1435)

Runs the forward pass.