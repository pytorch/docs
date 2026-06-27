# torch.nn.functional.max_pool1d

torch.nn.functional.max_pool1d(*input*, *kernel_size*, *stride=None*, *padding=0*, *dilation=1*, *ceil_mode=False*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/_jit_internal.py#L627)

Applies a 1D max pooling over an input signal composed of several input
planes.

Note

The order of `ceil_mode` and `return_indices` is different from
what seen in [`MaxPool1d`](torch.nn.MaxPool1d.html#torch.nn.MaxPool1d), and will change in a future release.

See [`MaxPool1d`](torch.nn.MaxPool1d.html#torch.nn.MaxPool1d) for details.

Parameters:

- **input** - input tensor of shape (minibatch,in_channels,iW)(\text{minibatch} , \text{in\_channels} , iW)(minibatch,in_channels,iW), minibatch dim optional.
- **kernel_size** - the size of the window. Can be a single number or a
tuple (kW,)
- **stride** - the stride of the window. Can be a single number or a tuple
(sW,). Default: `kernel_size`
- **padding** - Implicit negative infinity padding to be added on both sides, must be >= 0 and <= kernel_size / 2.
- **dilation** - The stride between elements within a sliding window, must be > 0.
- **ceil_mode** - If `True`, will use ceil instead of floor to compute the output shape. This
ensures that every element in the input tensor is covered by a sliding window.
- **return_indices** - If `True`, will return the argmax along with the max values.
Useful for [`torch.nn.functional.max_unpool1d`](torch.nn.functional.max_unpool1d.html#torch.nn.functional.max_unpool1d) later