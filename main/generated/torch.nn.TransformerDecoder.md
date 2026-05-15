# TransformerDecoder

*class*torch.nn.TransformerDecoder(*decoder_layer*, *num_layers*, *norm=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/nn/modules/transformer.py#L554)

TransformerDecoder is a stack of N decoder layers.

This TransformerDecoder layer implements the original architecture described
in the [Attention Is All You Need](https://arxiv.org/abs/1706.03762) paper. The
intent of this layer is as a reference implementation for foundational understanding
and thus it contains only limited features relative to newer Transformer architectures.
Given the fast pace of innovation in transformer-like architectures, we recommend
exploring this [tutorial](https://pytorch.org/tutorials/intermediate/transformer_building_blocks.html)
to build efficient layers from building blocks in core or using higher
level libraries from the [PyTorch Ecosystem](https://landscape.pytorch.org/).

Warning

All layers in the TransformerDecoder are initialized with the same parameters.
It is recommended to manually initialize the layers after creating the TransformerDecoder instance.

Parameters:

- **decoder_layer** ([*TransformerDecoderLayer*](torch.nn.TransformerDecoderLayer.html#torch.nn.TransformerDecoderLayer)) - an instance of the TransformerDecoderLayer() class (required).
- **num_layers** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of sub-decoder-layers in the decoder (required).
- **norm** ([*Module*](torch.nn.Module.html#torch.nn.Module)*|**None*) - the layer normalization component (optional).

Examples

```
>>> decoder_layer = nn.TransformerDecoderLayer(d_model=512, nhead=8)
>>> transformer_decoder = nn.TransformerDecoder(decoder_layer, num_layers=6)
>>> memory = torch.rand(10, 32, 512)
>>> tgt = torch.rand(20, 32, 512)
>>> out = transformer_decoder(tgt, memory)
```

forward(*tgt*, *memory*, *tgt_mask=None*, *memory_mask=None*, *tgt_key_padding_mask=None*, *memory_key_padding_mask=None*, *tgt_is_causal=None*, *memory_is_causal=False*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/nn/modules/transformer.py#L597)

Pass the inputs (and mask) through the decoder layer in turn.

Parameters:

- **tgt** ([*Tensor*](../tensors.html#torch.Tensor)) - the sequence to the decoder (required).
- **memory** ([*Tensor*](../tensors.html#torch.Tensor)) - the sequence from the last layer of the encoder (required).
- **tgt_mask** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - the mask for the tgt sequence (optional).
- **memory_mask** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - the mask for the memory sequence (optional).
- **tgt_key_padding_mask** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - the mask for the tgt keys per batch (optional).
- **memory_key_padding_mask** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - the mask for the memory keys per batch (optional).
- **tgt_is_causal** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*|**None*) - If specified, applies a causal mask as `tgt mask`.
Default: `None`; try to detect a causal mask.
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