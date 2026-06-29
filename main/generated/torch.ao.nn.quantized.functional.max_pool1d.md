# max_pool1d

*class*torch.ao.nn.quantized.functional.max_pool1d(*input*, *kernel_size*, *stride=None*, *padding=0*, *dilation=1*, *ceil_mode=False*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/12a9ea264bf805a66cd87e19e767ab23c2f59fef/torch/ao/nn/quantized/functional.py#L477)

Applies a 1D max pooling over a quantized input signal composed of
several quantized input planes.

Note

The input quantization parameters are propagated to the output.

See `MaxPool1d` for details.