# torch.utils.flop_counter.sdpa_backward_flop

torch.utils.flop_counter.sdpa_backward_flop(*grad_out_shape*, *query_shape*, *key_shape*, *value_shape*, **args*, *out_shape=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/55d182046edce7face6d9eb894f23b3a2588d876/torch/utils/flop_counter.py#L630)

Count flops for self-attention backward.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)