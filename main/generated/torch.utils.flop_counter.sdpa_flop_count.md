# torch.utils.flop_counter.sdpa_flop_count

torch.utils.flop_counter.sdpa_flop_count(*query_shape*, *key_shape*, *value_shape*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/utils/flop_counter.py#L420)

Count flops for self-attention.

Supports GQA (grouped-query attention) where key/value have fewer heads
than the query. The kernel broadcasts KV heads to match query heads.