# MultiheadAttention

*class*torch.nn.MultiheadAttention(*embed_dim*, *num_heads*, *dropout=0.0*, *bias=True*, *add_bias_kv=False*, *add_zero_attn=False*, *kdim=None*, *vdim=None*, *batch_first=False*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/2ba6a0a1865e48bce91c6a36d4d11218b52baee7/torch/nn/modules/activation.py#L1090)

Allows the model to jointly attend to information from different representation subspaces.

This MultiheadAttention layer implements the original architecture described
in the [Attention Is All You Need](https://arxiv.org/abs/1706.03762) paper. The
intent of this layer is as a reference implementation for foundational understanding
and thus it contains only limited features relative to newer architectures.
Given the fast pace of innovation in transformer-like architectures, we recommend
exploring this [tutorial](https://pytorch.org/tutorials/intermediate/transformer_building_blocks.html)
to build efficient layers from building blocks in core or using higher
level libraries from the [PyTorch Ecosystem](https://landscape.pytorch.org/).

Multi-Head Attention is defined as:

MultiHead(Q,K,V)=Concat(head1,...,headh)WO\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1,\dots,\text{head}_h)W^O

MultiHead(Q,K,V)=Concat(head1​,...,headh​)WO

where headi=Attention(QWiQ,KWiK,VWiV)\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)headi​=Attention(QWiQ​,KWiK​,VWiV​).

`nn.MultiheadAttention` will use the optimized implementations of
`scaled_dot_product_attention()` when possible.

In addition to support for the new `scaled_dot_product_attention()`
function, for speeding up Inference, MHA will use
fastpath inference with support for Nested Tensors, iff:

- self attention is being computed (i.e., `query`, `key`, and `value` are the same tensor).
- inputs are batched (3D) with `batch_first==True`
- Either autograd is disabled (using `torch.inference_mode` or `torch.no_grad`) or no tensor argument `requires_grad`
- training is disabled (using `.eval()`)
- `add_bias_kv` is `False`
- `add_zero_attn` is `False`
- `kdim` and `vdim` are equal to `embed_dim`
- if a [NestedTensor](https://pytorch.org/docs/stable/nested.html) is passed, neither `key_padding_mask`
nor `attn_mask` is passed
- autocast is disabled

If the optimized inference fastpath implementation is in use, a
[NestedTensor](https://pytorch.org/docs/stable/nested.html) can be passed for
`query`/`key`/`value` to represent padding more efficiently than using a
padding mask. In this case, a [NestedTensor](https://pytorch.org/docs/stable/nested.html)
will be returned, and an additional speedup proportional to the fraction of the input
that is padding can be expected.

Parameters:

- **embed_dim** - Total dimension of the model.
- **num_heads** - Number of parallel attention heads. Note that `embed_dim` will be split
across `num_heads` (i.e. each head will have dimension `embed_dim // num_heads`).
- **dropout** - Dropout probability on `attn_output_weights`. Default: `0.0` (no dropout).
- **bias** - If specified, adds bias to input / output projection layers. Default: `True`.
- **add_bias_kv** - If specified, adds bias to the key and value sequences at dim=0. Default: `False`.
- **add_zero_attn** - If specified, adds a new batch of zeros to the key and value sequences at dim=1.
Default: `False`.
- **kdim** - Total number of features for keys. Default: `None` (uses `kdim=embed_dim`).
- **vdim** - Total number of features for values. Default: `None` (uses `vdim=embed_dim`).
- **batch_first** - If `True`, then the input and output tensors are provided
as (batch, seq, feature). Default: `False` (seq, batch, feature).

Examples:

```
>>> multihead_attn = nn.MultiheadAttention(embed_dim, num_heads)
>>> attn_output, attn_output_weights = multihead_attn(query, key, value)
```

forward(*query*, *key*, *value*, *key_padding_mask=None*, *need_weights=True*, *attn_mask=None*, *average_attn_weights=True*, *is_causal=False*)[[source]](https://github.com/pytorch/pytorch/blob/2ba6a0a1865e48bce91c6a36d4d11218b52baee7/torch/nn/modules/activation.py#L1256)

Compute attention outputs using query, key, and value embeddings.

> Supports optional parameters for padding, masks and attention weights.

Parameters:

- **query** ([*Tensor*](../tensors.html#torch.Tensor)) - Query embeddings of shape (L,Eq)(L, E_q)(L,Eq​) for unbatched input, (L,N,Eq)(L, N, E_q)(L,N,Eq​) when `batch_first=False`
or (N,L,Eq)(N, L, E_q)(N,L,Eq​) when `batch_first=True`, where LLL is the target sequence length,
NNN is the batch size, and EqE_qEq​ is the query embedding dimension `embed_dim`.
Queries are compared against key-value pairs to produce the output.
See "Attention Is All You Need" for more details.
- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - Key embeddings of shape (S,Ek)(S, E_k)(S,Ek​) for unbatched input, (S,N,Ek)(S, N, E_k)(S,N,Ek​) when `batch_first=False`
or (N,S,Ek)(N, S, E_k)(N,S,Ek​) when `batch_first=True`, where SSS is the source sequence length,
NNN is the batch size, and EkE_kEk​ is the key embedding dimension `kdim`.
See "Attention Is All You Need" for more details.
- **value** ([*Tensor*](../tensors.html#torch.Tensor)) - Value embeddings of shape (S,Ev)(S, E_v)(S,Ev​) for unbatched input, (S,N,Ev)(S, N, E_v)(S,N,Ev​) when
`batch_first=False` or (N,S,Ev)(N, S, E_v)(N,S,Ev​) when `batch_first=True`, where SSS is the source
sequence length, NNN is the batch size, and EvE_vEv​ is the value embedding dimension `vdim`.
See "Attention Is All You Need" for more details.
- **key_padding_mask** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - If specified, a mask of shape (N,S)(N, S)(N,S) indicating which elements within `key`
to ignore for the purpose of attention (i.e. treat as "padding"). For unbatched query, shape should be (S)(S)(S).
Binary and float masks are supported.
For a binary mask, a `True` value indicates that the corresponding `key` value will be ignored for
the purpose of attention. For a float mask, it will be directly added to the corresponding `key` value.
- **need_weights** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If specified, returns `attn_output_weights` in addition to `attn_outputs`.
Set `need_weights=False` to use the optimized `scaled_dot_product_attention`
and achieve the best performance for MHA.
Default: `True`.
- **attn_mask** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - If specified, a 2D or 3D mask preventing attention to certain positions. Must be of shape
(L,S)(L, S)(L,S) or (N⋅num_heads,L,S)(N\cdot\text{num\_heads}, L, S)(N⋅num_heads,L,S), where NNN is the batch size,
LLL is the target sequence length, and SSS is the source sequence length. A 2D mask will be
broadcasted across the batch while a 3D mask allows for a different mask for each entry in the batch.
Binary and float masks are supported. For a binary mask, a `True` value indicates that the
corresponding position is not allowed to attend. For a float mask, the mask values will be added to
the attention weight.
If both attn_mask and key_padding_mask are supplied, their types should match.
- **average_attn_weights** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If true, indicates that the returned `attn_weights` should be averaged across
heads. Otherwise, `attn_weights` are provided separately per head. Note that this flag only has an
effect when `need_weights=True`. Default: `True` (i.e. average weights across heads)
- **is_causal** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If specified, applies a causal mask as attention mask.
Default: `False`.
Warning:
`is_causal` provides a hint that `attn_mask` is the
causal mask. Providing incorrect hints can result in
incorrect execution, including forward and backward
compatibility.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Tensor*](../tensors.html#torch.Tensor), [*Tensor*](../tensors.html#torch.Tensor) | None]

Outputs:

- **attn_output** - Attention outputs of shape (L,E)(L, E)(L,E) when input is unbatched,
(L,N,E)(L, N, E)(L,N,E) when `batch_first=False` or (N,L,E)(N, L, E)(N,L,E) when `batch_first=True`,
where LLL is the target sequence length, NNN is the batch size, and EEE is the
embedding dimension `embed_dim`.
- **attn_output_weights** - Only returned when `need_weights=True`. If `average_attn_weights=True`,
returns attention weights averaged across heads of shape (L,S)(L, S)(L,S) when input is unbatched or
(N,L,S)(N, L, S)(N,L,S), where NNN is the batch size, LLL is the target sequence length, and
SSS is the source sequence length. If `average_attn_weights=False`, returns attention weights per
head of shape (num_heads,L,S)(\text{num\_heads}, L, S)(num_heads,L,S) when input is unbatched or (N,num_heads,L,S)(N, \text{num\_heads}, L, S)(N,num_heads,L,S).

Note

batch_first argument is ignored for unbatched inputs.

merge_masks(*attn_mask*, *key_padding_mask*, *query*)[[source]](https://github.com/pytorch/pytorch/blob/2ba6a0a1865e48bce91c6a36d4d11218b52baee7/torch/nn/modules/activation.py#L1525)

Determine mask type and combine masks if necessary.

If only one mask is provided, that mask
and the corresponding mask type will be returned. If both masks are provided, they will be both
expanded to shape `(batch_size, num_heads, seq_len, seq_len)`, combined with logical `or`
and mask type 2 will be returned
:param attn_mask: attention mask of shape `(seq_len, seq_len)`, mask type 0
:param key_padding_mask: padding mask of shape `(batch_size, seq_len)`, mask type 1
:param query: query embeddings of shape `(batch_size, seq_len, embed_dim)`

Returns:

merged mask
mask_type: merged mask type (0, 1, or 2)

Return type:

merged_mask