# MaxUnpool3d

*class*torch.nn.modules.pooling.MaxUnpool3d(*kernel_size*, *stride=None*, *padding=0*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/nn/modules/pooling.py#L503)

Computes a partial inverse of [`MaxPool3d`](torch.nn.modules.pooling.MaxPool3d.html#torch.nn.modules.pooling.MaxPool3d).

[`MaxPool3d`](torch.nn.modules.pooling.MaxPool3d.html#torch.nn.modules.pooling.MaxPool3d) is not fully invertible, since the non-maximal values are lost.
`MaxUnpool3d` takes in as input the output of [`MaxPool3d`](torch.nn.modules.pooling.MaxPool3d.html#torch.nn.modules.pooling.MaxPool3d)
including the indices of the maximal values and computes a partial inverse
in which all non-maximal values are set to zero.

Note

This operation may behave nondeterministically when the input indices has repeat values.
See [pytorch/pytorch#80827](https://github.com/pytorch/pytorch/issues/80827) and [Reproducibility](../notes/randomness.html) for more information.

Note

[`MaxPool3d`](torch.nn.modules.pooling.MaxPool3d.html#torch.nn.modules.pooling.MaxPool3d) can map several input sizes to the same output
sizes. Hence, the inversion process can get ambiguous.
To accommodate this, you can provide the needed output size
as an additional argument `output_size` in the forward call.
See the Inputs section below.

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Size of the max pooling window.
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Stride of the max pooling window.
It is set to `kernel_size` by default.
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Padding that was added to the input

Inputs:

- input: the input Tensor to invert
- indices: the indices given out by [`MaxPool3d`](torch.nn.MaxPool3d.html#torch.nn.MaxPool3d)
- output_size (optional): the targeted output size

Shape:

- Input: (N,C,Din,Hin,Win)(N, C, D_{in}, H_{in}, W_{in})(N,C,Din​,Hin​,Win​) or (C,Din,Hin,Win)(C, D_{in}, H_{in}, W_{in})(C,Din​,Hin​,Win​).
- Output: (N,C,Dout,Hout,Wout)(N, C, D_{out}, H_{out}, W_{out})(N,C,Dout​,Hout​,Wout​) or (C,Dout,Hout,Wout)(C, D_{out}, H_{out}, W_{out})(C,Dout​,Hout​,Wout​), where

Dout=(Din−1)×stride[0]−2×padding[0]+kernel_size[0]D_{out} = (D_{in} - 1) \times \text{stride[0]} - 2 \times \text{padding[0]} + \text{kernel\_size[0]}

Dout​=(Din​−1)×stride[0]−2×padding[0]+kernel_size[0]
Hout=(Hin−1)×stride[1]−2×padding[1]+kernel_size[1]H_{out} = (H_{in} - 1) \times \text{stride[1]} - 2 \times \text{padding[1]} + \text{kernel\_size[1]}

Hout​=(Hin​−1)×stride[1]−2×padding[1]+kernel_size[1]
Wout=(Win−1)×stride[2]−2×padding[2]+kernel_size[2]W_{out} = (W_{in} - 1) \times \text{stride[2]} - 2 \times \text{padding[2]} + \text{kernel\_size[2]}

Wout​=(Win​−1)×stride[2]−2×padding[2]+kernel_size[2]

or as given by `output_size` in the call operator

Example:

```
>>> # pool of square window of size=3, stride=2
>>> pool = nn.MaxPool3d(3, stride=2, return_indices=True)
>>> unpool = nn.MaxUnpool3d(3, stride=2)
>>> output, indices = pool(torch.randn(20, 16, 51, 33, 15))
>>> unpooled_output = unpool(output, indices)
>>> unpooled_output.size()
torch.Size([20, 16, 51, 33, 15])
```

forward(*input*, *indices*, *output_size=None*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/nn/modules/pooling.py#L573)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)