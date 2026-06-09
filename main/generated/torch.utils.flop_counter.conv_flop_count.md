# torch.utils.flop_counter.conv_flop_count

torch.utils.flop_counter.conv_flop_count(*x_shape*, *w_shape*, *out_shape*, *transposed=False*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/utils/flop_counter.py#L131)

Count flops for convolution.

Note only multiplication is
counted. Computation for bias are ignored.
Flops for a transposed convolution are calculated as
flops = (x_shape[2:] * prod(w_shape) * batch_size).
:param x_shape: The input shape before convolution.
:type x_shape: list(int)
:param w_shape: The filter shape.
:type w_shape: list(int)
:param out_shape: The output shape after convolution.
:type out_shape: list(int)
:param transposed: is the convolution transposed
:type transposed: bool

Returns:

the number of flops

Return type:

[int](https://docs.python.org/3/library/functions.html#int)