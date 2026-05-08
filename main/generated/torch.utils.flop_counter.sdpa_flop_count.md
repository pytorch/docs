# torch.utils.flop_counter.sdpa_flop_count

torch.utils.flop_counter.sdpa_flop_count(*query_shape*, *key_shape*, *value_shape*)[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/utils/flop_counter.py#L284)

Count flops for self-attention.

Supports GQA (grouped-query attention) where key/value have fewer heads
than the query. The kernel broadcasts KV heads to match query heads.