# TransformerDecoderLayer

*class*torch.nn.modules.transformer.TransformerDecoderLayer(*d_model*, *nhead*, *dim_feedforward=2048*, *dropout=0.1*, *activation=<function relu>*, *layer_norm_eps=1e-05*, *batch_first=False*, *norm_first=False*, *bias=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/nn/modules/transformer.py#L981)

TransformerDecoderLayer is made up of self-attn, multi-head-attn and feedforward network.

This TransformerDecoderLayer implements the original architecture described
in the [Attention Is All You Need](https://arxiv.org/abs/1706.03762) paper. The
intent of this layer is as a reference implementation for foundational understanding
and thus it contains only limited features relative to newer Transformer architectures.
Given the fast pace of innovation in transformer-like architectures, we recommend
exploring this [tutorial](https://pytorch.org/tutorials/intermediate/transformer_building_blocks.html)
to build efficient layers from building blocks in core or using higher
level libraries from the [PyTorch Ecosystem](https://landscape.pytorch.org/).

Parameters:

- **d_model** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of expected features in the input (required).
- **nhead** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of heads in the multiheadattention models (required).
- **dim_feedforward** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the dimension of the feedforward network model (default=2048).
- **dropout** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the dropout value (default=0.1).
- **activation** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[*[*Tensor*](../tensors.html#torch.Tensor)*]**,*[*Tensor*](../tensors.html#torch.Tensor)*]*) - the activation function of the intermediate layer, can be a string
("relu" or "gelu") or a unary callable. Default: relu
- **layer_norm_eps** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the eps value in layer normalization components (default=1e-5).
- **batch_first** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True`, then the input and output tensors are provided
as (batch, seq, feature). Default: `False` (seq, batch, feature).
- **norm_first** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, layer norm is done prior to self attention, multihead
attention and feedforward operations, respectively. Otherwise it's done after.
Default: `False` (after).
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to `False`, `Linear` and `LayerNorm` layers will not learn an additive
bias. Default: `True`.

Examples

```
>>> decoder_layer = nn.TransformerDecoderLayer(d_model=512, nhead=8)
>>> memory = torch.rand(10, 32, 512)
>>> tgt = torch.rand(20, 32, 512)
>>> out = decoder_layer(tgt, memory)
```

Alternatively, when `batch_first` is `True`:

```
>>> decoder_layer = nn.TransformerDecoderLayer(
... d_model=512, nhead=8, batch_first=True
... )
>>> memory = torch.rand(32, 10, 512)
>>> tgt = torch.rand(32, 20, 512)
>>> out = decoder_layer(tgt, memory)
```

forward(*tgt*, *memory*, *tgt_mask=None*, *memory_mask=None*, *tgt_key_padding_mask=None*, *memory_key_padding_mask=None*, *tgt_is_causal=False*, *memory_is_causal=False*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/nn/modules/transformer.py#L1082)

Pass the inputs (and mask) through the decoder layer.

Parameters:

- **tgt** ([*Tensor*](../tensors.html#torch.Tensor)) - the sequence to the decoder layer (required).
- **memory** ([*Tensor*](../tensors.html#torch.Tensor)) - the sequence from the last layer of the encoder (required).
- **tgt_mask** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - the mask for the tgt sequence (optional).
- **memory_mask** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - the mask for the memory sequence (optional).
- **tgt_key_padding_mask** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - the mask for the tgt keys per batch (optional).
- **memory_key_padding_mask** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - the mask for the memory keys per batch (optional).
- **tgt_is_causal** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If specified, applies a causal mask as `tgt mask`.
Default: `False`.
Warning:
`tgt_is_causal` provides a hint that `tgt_mask` is
the causal mask. Providing incorrect hints can result in
incorrect execution, including forward and backward
compatibility.
- **memory_is_causal** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If specified, applies a causal mask as
`memory mask`.
Default: `False`.
Warning:
`memory_is_causal` provides a hint that
`memory_mask` is the causal mask. Providing incorrect
hints can result in incorrect execution, including
forward and backward compatibility.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Shape:

see the docs in [`Transformer`](torch.nn.Transformer.html#torch.nn.Transformer).