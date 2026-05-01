# torch.utils.flop_counter.sdpa_backward_flop

torch.utils.flop_counter.sdpa_backward_flop(*grad_out_shape*, *query_shape*, *key_shape*, *value_shape*, **args*, *out_shape=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/utils/flop_counter.py#L538)

Count flops for self-attention backward.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)