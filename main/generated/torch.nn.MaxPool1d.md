# MaxPool1d

*class*torch.nn.MaxPool1d(*kernel_size*, *stride=None*, *padding=0*, *dilation=1*, *return_indices=False*, *ceil_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/nn/modules/pooling.py#L79)

Applies a 1D max pooling over an input signal composed of several input planes.

In the simplest case, the output value of the layer with input size (N,C,L)(N, C, L)(N,C,L)
and output (N,C,Lout)(N, C, L_{out})(N,C,Lout​) can be precisely described as:

out(Ni,Cj,k)=max⁡m=0,...,kernel_size−1input(Ni,Cj,stride×k+m)out(N_i, C_j, k) = \max_{m=0, \ldots, \text{kernel\_size} - 1}
 input(N_i, C_j, stride \times k + m)

out(Ni​,Cj​,k)=m=0,...,kernel_size−1max​input(Ni​,Cj​,stride×k+m)

If `padding` is non-zero, then the input is implicitly padded with negative infinity on both sides
for `padding` number of points. `dilation` is the stride between the elements within the
sliding window. This [link](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md) has a nice visualization of the pooling parameters.

Note

When ceil_mode=True, sliding windows are allowed to go off-bounds if they start within the left padding
or the input. Sliding windows that would start in the right padded region are ignored.

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - The size of the sliding window, must be > 0.
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - The stride of the sliding window, must be > 0. Default value is `kernel_size`.
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - Implicit negative infinity padding to be added on both sides, must be >= 0 and <= kernel_size / 2.
- **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - The stride between elements within a sliding window, must be > 0.
- **return_indices** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True`, will return the argmax along with the max values.
Useful for [`torch.nn.MaxUnpool1d`](torch.nn.MaxUnpool1d.html#torch.nn.MaxUnpool1d) later
- **ceil_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True`, will use ceil instead of floor to compute the output shape. This
ensures that every element in the input tensor is covered by a sliding window.

Shape:

- Input: (N,C,Lin)(N, C, L_{in})(N,C,Lin​) or (C,Lin)(C, L_{in})(C,Lin​).
- Output: (N,C,Lout)(N, C, L_{out})(N,C,Lout​) or (C,Lout)(C, L_{out})(C,Lout​),

where `ceil_mode = False`

Lout=⌊Lin+2×padding−dilation×(kernel_size−1)−1stride⌋+1L_{out} = \left\lfloor \frac{L_{in} + 2 \times \text{padding} - \text{dilation}
 \times (\text{kernel\_size} - 1) - 1}{\text{stride}}\right\rfloor + 1

Lout​=⌊strideLin​+2×padding−dilation×(kernel_size−1)−1​⌋+1

where `ceil_mode = True`

Lout=⌈Lin+2×padding−dilation×(kernel_size−1)−1+(stride−1)stride⌉+1L_{out} = \left\lceil \frac{L_{in} + 2 \times \text{padding} - \text{dilation}
 \times (\text{kernel\_size} - 1) - 1 + (stride - 1)}{\text{stride}}\right\rceil + 1

Lout​=⌈strideLin​+2×padding−dilation×(kernel_size−1)−1+(stride−1)​⌉+1
- Ensure that the last pooling starts inside the image, make Lout=Lout−1L_{out} = L_{out} - 1Lout​=Lout​−1
when (Lout−1)∗stride>=Lin+padding(L_{out} - 1) * \text{stride} >= L_{in} + \text{padding}(Lout​−1)∗stride>=Lin​+padding.

Examples:

```
>>> # pool of size=3, stride=2
>>> m = nn.MaxPool1d(3, stride=2)
>>> input = torch.randn(20, 16, 50)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/nn/modules/pooling.py#L142)

Runs the forward pass.