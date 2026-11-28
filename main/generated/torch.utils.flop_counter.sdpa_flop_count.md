# torch.utils.flop_counter.sdpa_flop_count

torch.utils.flop_counter.sdpa_flop_count(*query_shape*, *key_shape*, *value_shape*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/utils/flop_counter.py#L426)

Count flops for self-attention.

Supports GQA (grouped-query attention) where key/value have fewer heads
than the query. The kernel broadcasts KV heads to match query heads.
Leading batch dims may be any number and broadcast, as on MPS.