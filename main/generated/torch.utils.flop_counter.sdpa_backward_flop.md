# torch.utils.flop_counter.sdpa_backward_flop

torch.utils.flop_counter.sdpa_backward_flop(*grad_out_shape*, *query_shape*, *key_shape*, *value_shape*, **args*, *out_shape=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/15e96b281415c58d3acf5d63d86df9d68744ee16/torch/utils/flop_counter.py#L546)

Count flops for self-attention backward.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)