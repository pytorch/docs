# torch.utils.flop_counter.sdpa_flop_count

torch.utils.flop_counter.sdpa_flop_count(*query_shape*, *key_shape*, *value_shape*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/utils/flop_counter.py#L284)

Count flops for self-attention.

Supports GQA (grouped-query attention) where key/value have fewer heads
than the query. The kernel broadcasts KV heads to match query heads.