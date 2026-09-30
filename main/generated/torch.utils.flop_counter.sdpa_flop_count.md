# torch.utils.flop_counter.sdpa_flop_count

torch.utils.flop_counter.sdpa_flop_count(*query_shape*, *key_shape*, *value_shape*)[[source]](https://github.com/pytorch/pytorch/blob/c96c0d945cc30cd4317ca02911049a75e43972b7/torch/utils/flop_counter.py#L420)

Count flops for self-attention.

Supports GQA (grouped-query attention) where key/value have fewer heads
than the query. The kernel broadcasts KV heads to match query heads.