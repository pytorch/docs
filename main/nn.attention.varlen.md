# torch.nn.attention.varlen

Variable-length attention implementation using Flash Attention.

This module provides a high-level Python interface for variable-length attention
that calls into the optimized Flash Attention kernels.

torch.nn.attention.varlen.varlen_attn(*query*, *key*, *value*, *cu_seq_q*, *cu_seq_k*, *max_q*, *max_k*, ***, *return_aux=None*, *scale=None*, *window_size=(-1, -1)*, *enable_gqa=False*, *seqused_k=None*, *block_table=None*, *num_splits=None*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/nn/attention/varlen.py#L201)

Compute variable-length attention using Flash Attention.

This function is similar to scaled_dot_product_attention but optimized for
variable-length sequences using cumulative sequence position tensors.

Parameters:

- **query** ([*Tensor*](tensors.html#torch.Tensor)) - Query tensor; shape (Tq,Hq,D)(T_q, H_q, D)(Tq​,Hq​,D)
- **key** ([*Tensor*](tensors.html#torch.Tensor)) - Key tensor; shape (Tk,Hkv,D)(T_k, H_{kv}, D)(Tk​,Hkv​,D), or
(total_pages,page_size,Hkv,D)(\text{total\_pages}, \text{page\_size}, H_{kv}, D)(total_pages,page_size,Hkv​,D) when `block_table` is provided.
- **value** ([*Tensor*](tensors.html#torch.Tensor)) - Value tensor; shape (Tk,Hkv,D)(T_k, H_{kv}, D)(Tk​,Hkv​,D), or
(total_pages,page_size,Hkv,D)(\text{total\_pages}, \text{page\_size}, H_{kv}, D)(total_pages,page_size,Hkv​,D) when `block_table` is provided.
- **cu_seq_q** ([*Tensor*](tensors.html#torch.Tensor)) - Cumulative sequence positions for queries; shape (N+1,)(N+1,)(N+1,)
- **cu_seq_k** ([*Tensor*](tensors.html#torch.Tensor)) - Cumulative sequence positions for keys/values; shape (N+1,)(N+1,)(N+1,)
- **max_q** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Maximum query sequence length in the batch.
- **max_k** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Maximum key/value sequence length in the batch.
- **return_aux** (*Optional**[**AuxRequest**]*) - If not None and `return_aux.lse` is True, also returns the logsumexp tensor.
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Scaling factor for attention scores
- **window_size** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - Window size for sliding window attention as (left, right).
Use (-1, -1) for full attention (default), (-1, 0) for causal attention,
or (W, 0) for causal attention with sliding window of size W.
- **enable_gqa** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to True, enables Grouped Query Attention (GQA)
and allows key/value to have fewer heads than query.
Each KV head is shared by a group of Hq/HkvH_q / H_{kv}Hq​/Hkv​ query heads,
so HqH_qHq​ must be divisible by HkvH_{kv}Hkv​.
Default is False.
- **seqused_k** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - Number of valid KV tokens per batch element; shape (N,)(N,)(N,).
When set, only the first `seqused_k[i]` tokens in the key/value sequence for batch
element *i* participate in attention. Useful for KV-cache decoding where the cache slot
is larger than the actual sequence. Inference-only (not supported in backward).
- **block_table** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) -

Block table for paged KV cache; shape
(N,max_pages_per_seq)(N, \text{max\_pages\_per\_seq})(N,max_pages_per_seq), dtype `int32`.
Requires `seqused_k`. Inference-only (not supported in backward).

When `block_table` is provided, `key` and `value` are a "pool" of
pages of tokens of KV data and the pages belong to any sequence/order.
The `block_table` is what maps each sequence's logical chunks
back to physical pages in this pool.

`seqused_k[i]` tells the kernel how many tokens in sequence *i* are
actually valid, since the last page is typically only partially filled.
- **num_splits** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Number of splits for split-KV. Set to `1`
to disable split-KV which enables batch invariance. Split-KV
parallelizes the key/value sequence dimension across multiple thread
blocks and combines partial results. The split decision depends
on `max_k` (the longest sequence in the batch), so different batch
compositions can change the reduction order and produce different
floating-point results for the same sequence. When this is disabled,
bitwise identical outputs are guaranteed for a given sequence
regardless of what other sequences are in the batch, at the
cost of lower GPU utilization when there are few queries. When
`None` (default), the kernel chooses automatically.

Returns:

Output tensor from attention computation; shape (Tq,Hq,D)(T_q, H_q, D)(Tq​,Hq​,D).

If `return_aux` is not None and `return_aux.lse` is True:

lse (Tensor): Log-sum-exp of attention scores; shape (Tq,Hq)(T_q, H_q)(Tq​,Hq​).

Return type:

output ([Tensor](tensors.html#torch.Tensor))

Shape legend:

- NNN: Batch size
- TqT_qTq​: Total number of query tokens in the batch (sum of all query sequence lengths)
- TkT_kTk​: Total number of key/value tokens in the batch (sum of all key/value sequence lengths)
- HqH_qHq​: Number of query attention heads
- HkvH_{kv}Hkv​: Number of key/value attention heads (equal to HqH_qHq​ unless GQA is enabled)
- DDD: Head dimension

Example:

```
>>> batch_size, max_seq_len, embed_dim, num_heads = 2, 512, 1024, 16
>>> head_dim = embed_dim // num_heads
>>> seq_lengths = []
>>> for _ in range(batch_size):
... length = torch.randint(1, max_seq_len // 64 + 1, (1,)).item() * 64
... seq_lengths.append(min(length, max_seq_len))
>>> seq_lengths = torch.tensor(seq_lengths, device="cuda")
>>> total_tokens = seq_lengths.sum().item()
>>>
>>> # Create packed query, key, value tensors
>>> query = torch.randn(
... total_tokens, num_heads, head_dim, dtype=torch.float16, device="cuda"
... )
>>> key = torch.randn(
... total_tokens, num_heads, head_dim, dtype=torch.float16, device="cuda"
... )
>>> value = torch.randn(
... total_tokens, num_heads, head_dim, dtype=torch.float16, device="cuda"
... )
>>>
>>> # Build cumulative sequence tensor
>>> cu_seq = torch.zeros(batch_size + 1, device="cuda", dtype=torch.int32)
>>> cu_seq[1:] = seq_lengths.cumsum(0)
>>> max_len = seq_lengths.max().item()
>>>
>>> # Call varlen_attn
>>> output = varlen_attn(
... query, key, value, cu_seq, cu_seq, max_len, max_len
... )
```

torch.nn.attention.varlen.varlen_attn_out(*out*, *query*, *key*, *value*, *cu_seq_q*, *cu_seq_k*, *max_q*, *max_k*, ***, *return_aux=None*, *scale=None*, *window_size=(-1, -1)*, *enable_gqa=False*, *seqused_k=None*, *block_table=None*, *num_splits=None*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/nn/attention/varlen.py#L432)

Compute variable-length attention using Flash Attention with a pre-allocated output tensor.

Same as `varlen_attn()` but writes the attention output into the provided `out` tensor
instead of allocating a new one.

Return type:

[*Tensor*](tensors.html#torch.Tensor) | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Tensor*](tensors.html#torch.Tensor), [*Tensor*](tensors.html#torch.Tensor)]

*class*torch.nn.attention.varlen.AuxRequest(*lse=False*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/nn/attention/varlen.py#L69)

Request which auxiliary outputs to compute from varlen_attn.

Each field is a boolean indicating whether that auxiliary output should be computed.