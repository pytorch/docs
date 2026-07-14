# torch.nn.attention.bias.CausalBias

*class*torch.nn.attention.bias.CausalBias(*variant*, *seq_len_q*, *seq_len_kv*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/nn/attention/bias.py#L86)

A bias representing causal attention patterns. For an overview of the bias structure, see the [`CausalVariant`](torch.nn.attention.bias.CausalVariant.html#torch.nn.attention.bias.CausalVariant) enum.

This class is used for defining causal (triangular) attention biases. For constructing the bias, there exist
two factory functions: [`causal_upper_left()`](torch.nn.attention.bias.causal_upper_left.html#torch.nn.attention.bias.causal_upper_left) and [`causal_lower_right()`](torch.nn.attention.bias.causal_lower_right.html#torch.nn.attention.bias.causal_lower_right).

Example:

```
from torch.nn.attention.bias import causal_lower_right

bsz, num_heads, seqlen_q, seqlen_kv, head_dim = 32, 8, 4, 12, 8

# Create a lower-right causal bias
attn_bias = causal_lower_right(seqlen_q, seqlen_kv)

q = torch.randn(
 bsz, num_heads, seqlen_q, head_dim, device="cuda", dtype=torch.float16
)
k = torch.randn(
 bsz, num_heads, seqlen_kv, head_dim, device="cuda", dtype=torch.float16
)
v = torch.randn(
 bsz, num_heads, seqlen_kv, head_dim, device="cuda", dtype=torch.float16
)

out = F.scaled_dot_product_attention(q, k, v, attn_bias)
```

Warning

This class is a prototype and subject to change.