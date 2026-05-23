# torch.utils.flop_counter.sdpa_backward_flop

torch.utils.flop_counter.sdpa_backward_flop(*grad_out_shape*, *query_shape*, *key_shape*, *value_shape*, **args*, *out_shape=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/utils/flop_counter.py#L546)

Count flops for self-attention backward.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)