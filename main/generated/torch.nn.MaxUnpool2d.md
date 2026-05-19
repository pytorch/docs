# MaxUnpool2d

*class*torch.nn.MaxUnpool2d(*kernel_size*, *stride=None*, *padding=0*)[[source]](https://github.com/pytorch/pytorch/blob/2700915a75e05f161593ddd3bb8f6c01c29b8777/torch/nn/modules/pooling.py#L407)

Computes a partial inverse of [`MaxPool2d`](torch.nn.MaxPool2d.html#torch.nn.MaxPool2d).

[`MaxPool2d`](torch.nn.MaxPool2d.html#torch.nn.MaxPool2d) is not fully invertible, since the non-maximal values are lost.

`MaxUnpool2d` takes in as input the output of [`MaxPool2d`](torch.nn.MaxPool2d.html#torch.nn.MaxPool2d)
including the indices of the maximal values and computes a partial inverse
in which all non-maximal values are set to zero.

Note

This operation may behave nondeterministically when the input indices has repeat values.
See [pytorch/pytorch#80827](https://github.com/pytorch/pytorch/issues/80827) and [Reproducibility](../notes/randomness.html) for more information.

Note

[`MaxPool2d`](torch.nn.MaxPool2d.html#torch.nn.MaxPool2d) can map several input sizes to the same output
sizes. Hence, the inversion process can get ambiguous.
To accommodate this, you can provide the needed output size
as an additional argument `output_size` in the forward call.
See the Inputs and Example below.

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Size of the max pooling window.
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Stride of the max pooling window.
It is set to `kernel_size` by default.
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - Padding that was added to the input

Inputs:

- input: the input Tensor to invert
- indices: the indices given out by [`MaxPool2d`](torch.nn.MaxPool2d.html#torch.nn.MaxPool2d)
- output_size (optional): the targeted output size

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H_{in}, W_{in})(C,Hin​,Win​).
- Output: (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) or (C,Hout,Wout)(C, H_{out}, W_{out})(C,Hout​,Wout​), where

Hout=(Hin−1)×stride[0]−2×padding[0]+kernel_size[0]H_{out} = (H_{in} - 1) \times \text{stride[0]} - 2 \times \text{padding[0]} + \text{kernel\_size[0]}

Hout​=(Hin​−1)×stride[0]−2×padding[0]+kernel_size[0]
Wout=(Win−1)×stride[1]−2×padding[1]+kernel_size[1]W_{out} = (W_{in} - 1) \times \text{stride[1]} - 2 \times \text{padding[1]} + \text{kernel\_size[1]}

Wout​=(Win​−1)×stride[1]−2×padding[1]+kernel_size[1]

or as given by `output_size` in the call operator

Example:

```
>>> pool = nn.MaxPool2d(2, stride=2, return_indices=True)
>>> unpool = nn.MaxUnpool2d(2, stride=2)
>>> input = torch.tensor([[[[ 1., 2., 3., 4.],
 [ 5., 6., 7., 8.],
 [ 9., 10., 11., 12.],
 [13., 14., 15., 16.]]]])
>>> output, indices = pool(input)
>>> unpool(output, indices)
tensor([[[[ 0., 0., 0., 0.],
 [ 0., 6., 0., 8.],
 [ 0., 0., 0., 0.],
 [ 0., 14., 0., 16.]]]])
>>> # Now using output_size to resolve an ambiguous size for the inverse
>>> input = torch.tensor([[[[ 1., 2., 3., 4., 5.],
 [ 6., 7., 8., 9., 10.],
 [11., 12., 13., 14., 15.],
 [16., 17., 18., 19., 20.]]]])
>>> output, indices = pool(input)
>>> # This call will not work without specifying output_size
>>> unpool(output, indices, output_size=input.size())
tensor([[[[ 0., 0., 0., 0., 0.],
 [ 0., 7., 0., 9., 0.],
 [ 0., 0., 0., 0., 0.],
 [ 0., 17., 0., 19., 0.]]]])
```

forward(*input*, *indices*, *output_size=None*)[[source]](https://github.com/pytorch/pytorch/blob/2700915a75e05f161593ddd3bb8f6c01c29b8777/torch/nn/modules/pooling.py#L494)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)