# torch.utils.flop_counter.sdpa_backward_flop

torch.utils.flop_counter.sdpa_backward_flop(*grad_out_shape*, *query_shape*, *key_shape*, *value_shape*, **args*, *out_shape=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/utils/flop_counter.py#L542)

Count flops for self-attention backward.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)