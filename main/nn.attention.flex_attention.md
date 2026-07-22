# torch.nn.attention.flex_attention

torch.nn.attention.flex_attention.flex_attention(*query: [Tensor](tensors.html#torch.Tensor)*, *key: [Tensor](tensors.html#torch.Tensor)*, *value: [Tensor](tensors.html#torch.Tensor)*, *score_mod: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor)], [Tensor](tensors.html#torch.Tensor)] | [None](https://docs.python.org/3/library/constants.html#None) = None*, *block_mask: BlockMask | [None](https://docs.python.org/3/library/constants.html#None) = None*, *scale: [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *enable_gqa: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *return_lse: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[False] = False*, *kernel_options: FlexKernelOptions | [None](https://docs.python.org/3/library/constants.html#None) = None*, ***, *return_aux: [None](https://docs.python.org/3/library/constants.html#None) = None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L2365)

torch.nn.attention.flex_attention.flex_attention(*query: [Tensor](tensors.html#torch.Tensor)*, *key: [Tensor](tensors.html#torch.Tensor)*, *value: [Tensor](tensors.html#torch.Tensor)*, *score_mod: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor)], [Tensor](tensors.html#torch.Tensor)] | [None](https://docs.python.org/3/library/constants.html#None) = None*, *block_mask: BlockMask | [None](https://docs.python.org/3/library/constants.html#None) = None*, *scale: [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *enable_gqa: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *return_lse: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True] = False*, *kernel_options: FlexKernelOptions | [None](https://docs.python.org/3/library/constants.html#None) = None*, ***, *return_aux: [None](https://docs.python.org/3/library/constants.html#None) = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor)]

torch.nn.attention.flex_attention.flex_attention(*query: [Tensor](tensors.html#torch.Tensor)*, *key: [Tensor](tensors.html#torch.Tensor)*, *value: [Tensor](tensors.html#torch.Tensor)*, *score_mod: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor)], [Tensor](tensors.html#torch.Tensor)] | [None](https://docs.python.org/3/library/constants.html#None) = None*, *block_mask: BlockMask | [None](https://docs.python.org/3/library/constants.html#None) = None*, *scale: [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *enable_gqa: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *return_lse: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *kernel_options: FlexKernelOptions | [None](https://docs.python.org/3/library/constants.html#None) = None*, ***, *return_aux: AuxRequest*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](tensors.html#torch.Tensor), AuxOutput]

torch.nn.attention.flex_attention.flex_attention(*query: [Tensor](tensors.html#torch.Tensor)*, *key: [Tensor](tensors.html#torch.Tensor)*, *value: [Tensor](tensors.html#torch.Tensor)*, *score_mod: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor)], [Tensor](tensors.html#torch.Tensor)] | [None](https://docs.python.org/3/library/constants.html#None) = None*, *block_mask: BlockMask | [None](https://docs.python.org/3/library/constants.html#None) = None*, *scale: [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *enable_gqa: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *return_lse: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True] = False*, *kernel_options: FlexKernelOptions | [None](https://docs.python.org/3/library/constants.html#None) = None*, ***, *return_aux: AuxRequest*) → Never

This function implements scaled dot product attention with an arbitrary attention score modification function
described in the [Flex Attention](https://arxiv.org/abs/2412.05496) paper. See also the
[blog post](https://pytorch.org/blog/flexattention/).

This function computes the scaled dot product attention between query, key, and value tensors with a user-defined
attention score modification function. The attention score modification function will be applied after the attention
scores have been calculated between the query and key tensors. The attention scores are calculated as follows:

The `score_mod` function should have the following signature:

```
def score_mod(
 score: Tensor,
 batch: Tensor,
 head: Tensor,
 q_idx: Tensor,
 k_idx: Tensor
) -> Tensor:
```

Where:

- `score`: A scalar tensor representing the attention score,
with the same data type and device as the query, key, and value tensors.
- `batch`, `head`, `q_idx`, `k_idx`: Scalar tensors indicating
the batch index, query head index, query index, and key/value index, respectively.
These should have the `torch.int` data type and be located on the same device as the score tensor.

Parameters:

- **query** ([*Tensor*](tensors.html#torch.Tensor)) - Query tensor; shape (B,Hq,L,E)(B, Hq, L, E)(B,Hq,L,E). For FP8 dtypes, should be in row-major memory layout for optimal performance.
- **key** ([*Tensor*](tensors.html#torch.Tensor)) - Key tensor; shape (B,Hkv,S,E)(B, Hkv, S, E)(B,Hkv,S,E). For FP8 dtypes, should be in row-major memory layout for optimal performance.
- **value** ([*Tensor*](tensors.html#torch.Tensor)) - Value tensor; shape (B,Hkv,S,Ev)(B, Hkv, S, Ev)(B,Hkv,S,Ev). For FP8 dtypes, should be in column-major memory layout for optimal performance.
- **score_mod** (*Optional**[**Callable**]*) - Function to modify attention scores. By default no score_mod is applied.
- **block_mask** (*Optional**[**BlockMask**]*) - BlockMask object that controls the blocksparsity pattern of the attention.
- **scale** (*Optional**[*[*float*](https://docs.python.org/3/library/functions.html#float)*]*) - Scaling factor applied prior to softmax. If none, the default value is set to 1E\frac{1}{\sqrt{E}}E​1​.
- **enable_gqa** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to True, enables Grouped Query Attention (GQA) and broadcasts key/value heads to query heads.
- **return_lse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to return the logsumexp of the attention scores. Default is False. **Deprecated**: Use `return_aux=AuxRequest(lse=True)` instead.
- **kernel_options** (*Optional**[**FlexKernelOptions**]*) - Options to control the behavior of the underlying Triton kernels.
See `FlexKernelOptions` for available options and usage examples.
- **return_aux** (*Optional**[**AuxRequest**]*) - Specifies which auxiliary outputs to compute and return.
If None, only the attention output is returned. Use `AuxRequest(lse=True, max_scores=True)`
to request both auxiliary outputs.

Returns:

Attention output; shape (B,Hq,L,Ev)(B, Hq, L, Ev)(B,Hq,L,Ev).

When `return_aux` is not None:

aux (AuxOutput): Auxiliary outputs with requested fields populated.

When `return_aux` is None (deprecated paths):

lse (Tensor): Log-sum-exp of attention scores; shape (B,Hq,L)(B, Hq, L)(B,Hq,L). Only returned if `return_lse=True`.

Return type:

output ([Tensor](tensors.html#torch.Tensor))

Shape legend:

- N:Batch size...:Any number of other batch dimensions (optional)N: \text{Batch size} ... : \text{Any number of other batch dimensions (optional)}N:Batch size...:Any number of other batch dimensions (optional)
- S:Source sequence lengthS: \text{Source sequence length}S:Source sequence length
- L:Target sequence lengthL: \text{Target sequence length}L:Target sequence length
- E:Embedding dimension of the query and keyE: \text{Embedding dimension of the query and key}E:Embedding dimension of the query and key
- Ev:Embedding dimension of the valueEv: \text{Embedding dimension of the value}Ev:Embedding dimension of the value

Warning

torch.nn.attention.flex_attention is a prototype feature in PyTorch.
Please look forward to a more stable implementation in a future version of PyTorch.
Read more about feature classification at: [https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

*class*torch.nn.attention.flex_attention.AuxOutput(*lse=None*, *max_scores=None*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L293)

Auxiliary outputs from flex_attention operation.

Fields will be None if not requested, or contain the tensor if requested.

*class*torch.nn.attention.flex_attention.AuxRequest(*lse=False*, *max_scores=False*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L283)

Request which auxiliary outputs to compute from flex_attention.

Each field is a boolean indicating whether that auxiliary output should be computed.

## BlockMask Utilities

torch.nn.attention.flex_attention.create_block_mask(*mask_mod*, *B*, *H*, *Q_LEN*, *KV_LEN*, *device=None*, *BLOCK_SIZE=128*, *_compile=False*, *separate_full_blocks=True*, *compute_dq_write_order=False*, *dq_kv_order=True*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L1967)

This function creates a block mask tuple from a mask_mod function.

Parameters:

- **mask_mod** (*Callable*) - mask_mod function. This is a callable that defines the
masking pattern for the attention mechanism. It takes four arguments:
b (batch size), h (number of heads), q_idx (query index), and kv_idx (key/value index).
It should return a boolean tensor indicating which attention connections are allowed (True)
or masked out (False).
- **B** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Batch size.
- **H** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of query heads.
- **Q_LEN** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Sequence length of query.
- **KV_LEN** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Sequence length of key/value.
- **device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Device to run the mask creation on.
- **BLOCK_SIZE** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - Block size for the block mask. If a single int is provided it is used for both query and key/value.
- **separate_full_blocks** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, fully unmasked blocks are stored
separately so kernels can skip mask_mod on those blocks. If False,
all non-empty blocks are stored as partial blocks and mask_mod is
applied to every block.
- **compute_dq_write_order** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, precompute dQ write-order
metadata needed by deterministic block-sparse FLASH backward.
- **dq_kv_order** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - KV-column scheduler order used for deterministic
dQ accumulation when compute_dq_write_order is True. False means
ascending n-block order and True means descending/SPT order.
Explicit tensor schedules are not supported by create_block_mask
yet; they are supported by BlockMask.from_kv_blocks for callers
that provide precomputed write-order metadata directly.

Returns:

A BlockMask object that contains the block mask information.

Return type:

BlockMask

Example Usage:

```
def causal_mask(b, h, q_idx, kv_idx):
 return q_idx >= kv_idx

block_mask = create_block_mask(causal_mask, 1, 1, 8192, 8192, device="cuda")
query = torch.randn(1, 1, 8192, 64, device="cuda", dtype=torch.float16)
key = torch.randn(1, 1, 8192, 64, device="cuda", dtype=torch.float16)
value = torch.randn(1, 1, 8192, 64, device="cuda", dtype=torch.float16)
output = flex_attention(query, key, value, block_mask=block_mask)
```

torch.nn.attention.flex_attention.create_mask(*mod_fn*, *B*, *H*, *Q_LEN*, *KV_LEN*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L1828)

This function creates a mask tensor from a mod_fn function.

Parameters:

- **mod_fn** (*Union**[**_score_mod_signature**,**_mask_mod_signature**]*) - Function to modify attention scores.
- **B** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Batch size.
- **H** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of query heads.
- **Q_LEN** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Sequence length of query.
- **KV_LEN** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Sequence length of key/value.
- **device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Device to run the mask creation on.

Returns:

A mask tensor with shape (B, H, M, N).

Return type:

mask ([Tensor](tensors.html#torch.Tensor))

torch.nn.attention.flex_attention.and_masks(**mask_mods*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L1773)

Returns a mask_mod that's the intersection of provided mask_mods

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Tensor*](tensors.html#torch.Tensor), [*Tensor*](tensors.html#torch.Tensor), [*Tensor*](tensors.html#torch.Tensor), [*Tensor*](tensors.html#torch.Tensor)], [*Tensor*](tensors.html#torch.Tensor)]

torch.nn.attention.flex_attention.or_masks(**mask_mods*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L1759)

Returns a mask_mod that's the union of provided mask_mods

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Tensor*](tensors.html#torch.Tensor), [*Tensor*](tensors.html#torch.Tensor), [*Tensor*](tensors.html#torch.Tensor), [*Tensor*](tensors.html#torch.Tensor)], [*Tensor*](tensors.html#torch.Tensor)]

torch.nn.attention.flex_attention.noop_mask(*batch*, *head*, *token_q*, *token_kv*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L407)

Returns a noop mask_mod

Return type:

[*Tensor*](tensors.html#torch.Tensor)

## FlexKernelOptions

*class*torch.nn.attention.flex_attention.FlexKernelOptions[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L144)

Options for controlling the behavior of FlexAttention kernels.

These options are passed to the underlying Triton kernels to control performance
and numerical behavior. Most users will not need to specify these options as the
default autotuning provides good performance.

The options can be prefixed with `fwd_` or `bwd_` to apply only to forward or
backward pass respectively. For example: `fwd_BLOCK_M` and `bwd_BLOCK_M1`.

Note

We currently do not provide any backward compatibility guarantees for these options.
That being said most of these have remained pretty stable since their introduction. But
We do not consider this part of the public API just yet. We think that some documentation
Is better than secret hidden flags, but we may change these options in the future.

Example Usage:

```
# Using dictionary (backward compatible)
kernel_opts = {"BLOCK_M": 64, "BLOCK_N": 64, "PRESCALE_QK": True}
output = flex_attention(q, k, v, kernel_options=kernel_opts)

# Using TypedDict (recommended for type safety)
from torch.nn.attention.flex_attention import FlexKernelOptions

kernel_opts: FlexKernelOptions = {
 "BLOCK_M": 64,
 "BLOCK_N": 64,
 "PRESCALE_QK": True,
}
output = flex_attention(q, k, v, kernel_options=kernel_opts)

# Forward/backward specific options
kernel_opts: FlexKernelOptions = {
 "fwd_BLOCK_M": 64,
 "bwd_BLOCK_M1": 32,
 "PRESCALE_QK": False,
}
output = flex_attention(q, k, v, kernel_options=kernel_opts)
```

BACKEND*: NotRequired[[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['AUTO', 'TRITON', 'FLASH', 'TRITON_DECODE']]*

Selects a specific kernel backend.

Options:

- "AUTO": Use current heuristics (typically Triton-based kernels with
automatic selection between flex_attention and flex_decoding)
- "TRITON": Standard Triton flex_attention kernel
- "TRITON_DECODE": Triton flex_decoding kernel, only available for short sequence lengths with specific configurations
- "FLASH": Experimental: Flash Attention kernel (cute-dsl), user needs to have flash installed

This option cannot be combined with legacy knobs such as `FORCE_USE_FLEX_ATTENTION`.
Raises an error if the requested backend cannot be used. Default: "AUTO"

BLOCKS_ARE_CONTIGUOUS*: NotRequired[[bool](https://docs.python.org/3/library/functions.html#bool)]*

If True, guarantees that all blocks in the mask are contiguous.
Allows optimizing block traversal. For example, causal masks would satisfy this,
but prefix_lm + sliding window would not. Default: False.

BLOCK_M*: NotRequired[[int](https://docs.python.org/3/library/functions.html#int)]*

Thread block size for the sequence length dimension of Q in forward pass.
Must be a power of 2. Common values: 16, 32, 64, 128. Default is determined by autotuning.

BLOCK_M1*: NotRequired[[int](https://docs.python.org/3/library/functions.html#int)]*

Thread block size for Q dimension in backward pass. Use as 'bwd_BLOCK_M1'.
Default is determined by autotuning.

BLOCK_M2*: NotRequired[[int](https://docs.python.org/3/library/functions.html#int)]*

Thread block size for second Q dimension in backward pass. Use as 'bwd_BLOCK_M2'.
Default is determined by autotuning.

BLOCK_N*: NotRequired[[int](https://docs.python.org/3/library/functions.html#int)]*

Thread block size for the sequence length dimension of K/V in forward pass.
Must be a power of 2. Common values: 16, 32, 64, 128. Default is determined by autotuning.

BLOCK_N1*: NotRequired[[int](https://docs.python.org/3/library/functions.html#int)]*

Thread block size for K/V dimension in backward pass. Use as 'bwd_BLOCK_N1'.
Default is determined by autotuning.

BLOCK_N2*: NotRequired[[int](https://docs.python.org/3/library/functions.html#int)]*

Thread block size for second K/V dimension in backward pass. Use as 'bwd_BLOCK_N2'.
Default is determined by autotuning.

FORCE_USE_FLEX_ATTENTION*: NotRequired[[bool](https://docs.python.org/3/library/functions.html#bool)]*

If True, forces the use of the flex attention kernel instead of potentially using
the more optimized flex-decoding kernel for short sequences. This can be a helpful
option for debugging. Default: False.

PRESCALE_QK*: NotRequired[[bool](https://docs.python.org/3/library/functions.html#bool)]*

Whether to pre-scale QK by 1/sqrt(d) and change of base. This is slightly faster but
may have more numerical error. Default: False.

ROWS_GUARANTEED_SAFE*: NotRequired[[bool](https://docs.python.org/3/library/functions.html#bool)]*

If True, guarantees that at least one value in each row is not masked out.
Allows skipping safety checks for better performance. Only set this if you are certain
your mask guarantees this property. For example, causal attention is guaranteed safe
because each query has at least 1 key-value to attend to. Default: False.

USE_TMA*: NotRequired[[bool](https://docs.python.org/3/library/functions.html#bool)]*

Whether to use Tensor Memory Accelerator (TMA) on supported hardware.
This is experimental and may not work on all hardware, currently specific
to NVIDIA GPUs Hopper+. Default: False.

WRITE_DQ*: NotRequired[[bool](https://docs.python.org/3/library/functions.html#bool)]*

Controls whether gradient scatters are done in the DQ iteration loop of the backward pass.
Setting this to False will force this to happen in the DK loop which depending on your
specific score_mod and mask_mod might be faster. Default: True.

kpack*: NotRequired[[int](https://docs.python.org/3/library/functions.html#int)]*

ROCm-specific kernel packing parameter.

matrix_instr_nonkdim*: NotRequired[[int](https://docs.python.org/3/library/functions.html#int)]*

ROCm-specific matrix instruction non-K dimension.

num_stages*: NotRequired[[int](https://docs.python.org/3/library/functions.html#int)]*

Number of pipeline stages in the CUDA kernel. Higher values may improve performance
but increase shared memory usage. Default is determined by autotuning.

num_warps*: NotRequired[[int](https://docs.python.org/3/library/functions.html#int)]*

Number of warps to use in the CUDA kernel. Higher values may improve performance
but increase register pressure. Default is determined by autotuning.

waves_per_eu*: NotRequired[[int](https://docs.python.org/3/library/functions.html#int)]*

ROCm-specific waves per execution unit.

## BlockMask

*class*torch.nn.attention.flex_attention.BlockMask(*seq_lengths*, *kv_num_blocks*, *kv_indices*, *full_kv_num_blocks*, *full_kv_indices*, *q_num_blocks*, *q_indices*, *full_q_num_blocks*, *full_q_indices*, *BLOCK_SIZE=(128*, *128)*, *mask_mod=<function noop_mask>*, ***, *dq_write_order=None*, *dq_write_order_full=None*, *dq_kv_order=None*, *dq_kv_order_spt=None*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L855)

BlockMask is our format for representing a block-sparse attention mask.
It is somewhat of a cross in-between BCSR and a non-sparse format.

**Basics**

A block-sparse mask means that instead of representing the sparsity of
individual elements in the mask, a KV_BLOCK_SIZE x Q_BLOCK_SIZE block is
considered sparse only if every element within that block is sparse.
This aligns well with hardware, which generally expects to perform
contiguous loads and computation.

This format is primarily optimized for 1. simplicity, and 2. kernel
efficiency. Notably, it is *not* optimized for size, as this mask is always
reduced by a factor of KV_BLOCK_SIZE * Q_BLOCK_SIZE. If the size is a
concern, the tensors can be reduced in size by increasing the block size.

The essentials of our format are:

num_blocks_in_row: Tensor[ROWS]:
Describes the number of blocks present in each row.

col_indices: Tensor[ROWS, MAX_BLOCKS_IN_COL]:
col_indices[i] is the sequence of block positions for row i. The values of
this row after col_indices[i][num_blocks_in_row[i]] are undefined.

For example, to reconstruct the original tensor from this format:

```
dense_mask = torch.zeros(ROWS, COLS)
for row in range(ROWS):
 for block_idx in range(num_blocks_in_row[row]):
 dense_mask[row, col_indices[row, block_idx]] = 1
```

Notably, this format makes it easier to implement a reduction along the
*rows* of the mask.

**Details**

The basics of our format require only kv_num_blocks and kv_indices. The
primary block-sparse layout is represented by up to 4 tensor pairs:

1. (kv_num_blocks, kv_indices): Used for the forwards pass of attention, as
we reduce along the KV dimension.

2. [OPTIONAL] (full_kv_num_blocks, full_kv_indices): This is optional and
purely an optimization. As it turns out, applying masking to every block
is quite expensive! If we specifically know which blocks are "full" and
don't require masking at all, then we can skip applying mask_mod to these
blocks. This requires the user to split out a separate mask_mod from the
score_mod. For causal masks, this is about a 15% speedup.

3. [GENERATED] (q_num_blocks, q_indices): Required for the backwards pass,
as computing dKV requires iterating along the mask along the Q dimension. These are autogenerated from 1.

4. [GENERATED] (full_q_num_blocks, full_q_indices): Same as above, but for
the backwards pass. These are autogenerated from 2.

Additional optional tensors may carry deterministic dQ metadata for
block-sparse FLASH backward:

5. [OPTIONAL] dq_write_order: Write-order metadata for partial blocks. This
is produced by create_block_mask when compute_dq_write_order=True, or passed
directly to BlockMask.from_kv_blocks by callers that precompute it.

6. [OPTIONAL] dq_write_order_full: Write-order metadata for full blocks,
produced or passed the same way as dq_write_order.

7. [OPTIONAL] dq_kv_order: Explicit KV scheduler order used to produce the
write-order metadata. create_block_mask currently accepts a boolean
dq_kv_order; BlockMask.from_kv_blocks also accepts a tensor for callers that
provide precomputed write-order metadata directly.

BLOCK_SIZE*: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]*

as_tuple(*flatten: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True] = True*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None), [int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int), [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor)], [Tensor](tensors.html#torch.Tensor)]][[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L1200)

as_tuple(*flatten: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[False]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)], [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None), [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)], [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor)], [Tensor](tensors.html#torch.Tensor)]]

Returns a tuple of the attributes of the BlockMask.

Parameters:

**flatten** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, it will flatten the tuple of (KV_BLOCK_SIZE, Q_BLOCK_SIZE)

dq_kv_order*: [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*

dq_kv_order_spt*: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None)*

dq_write_order*: [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*

dq_write_order_full*: [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*

*classmethod*from_kv_blocks(*kv_num_blocks*, *kv_indices*, *full_kv_num_blocks=None*, *full_kv_indices=None*, *BLOCK_SIZE=128*, *mask_mod=None*, *seq_lengths=None*, *compute_q_blocks=True*, ***, *dq_write_order=None*, *dq_write_order_full=None*, *dq_kv_order=None*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L1061)

Creates a BlockMask instance from key-value block information.

Parameters:

- **kv_num_blocks** ([*Tensor*](tensors.html#torch.Tensor)) - Number of kv_blocks in each Q_BLOCK_SIZE row tile.
- **kv_indices** ([*Tensor*](tensors.html#torch.Tensor)) - Indices of key-value blocks in each Q_BLOCK_SIZE row tile.
- **full_kv_num_blocks** (*Optional**[*[*Tensor*](tensors.html#torch.Tensor)*]*) - Number of full kv_blocks in each Q_BLOCK_SIZE row tile.
- **full_kv_indices** (*Optional**[*[*Tensor*](tensors.html#torch.Tensor)*]*) - Indices of full key-value blocks in each Q_BLOCK_SIZE row tile.
- **BLOCK_SIZE** (*Union**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]*) - Size of KV_BLOCK_SIZE x Q_BLOCK_SIZE tiles.
- **mask_mod** (*Optional**[**Callable**]*) - Function to modify the mask.
- **dq_write_order** (*Optional**[*[*Tensor*](tensors.html#torch.Tensor)*]*) - Precomputed deterministic dQ write-order metadata.
- **dq_write_order_full** (*Optional**[*[*Tensor*](tensors.html#torch.Tensor)*]*) - Precomputed deterministic dQ write-order metadata for full blocks.
- **dq_kv_order** (*Optional**[**Union**[*[*Tensor*](tensors.html#torch.Tensor)*,*[*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]*) - KV-column scheduler order used to produce dq_write_order. A bool selects a built-in order; a tensor gives an explicit scheduler-rank to n-block permutation.

Returns:

Instance with full Q information generated via _transposed_ordered

Return type:

BlockMask

Raises:

- [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If kv_indices has < 2 dimensions.
- [**AssertionError**](https://docs.python.org/3/library/exceptions.html#AssertionError) - If only one of full_kv_* args is provided.

full_kv_indices*: [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*

full_kv_num_blocks*: [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*

full_q_indices*: [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*

full_q_num_blocks*: [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*

kv_indices*: [Tensor](tensors.html#torch.Tensor)*

kv_num_blocks*: [Tensor](tensors.html#torch.Tensor)*

mask_mod*: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor), [Tensor](tensors.html#torch.Tensor)], [Tensor](tensors.html#torch.Tensor)]*

numel()[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L1437)

Returns the number of elements (not accounting for sparsity) in the mask.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

q_indices*: [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*

q_num_blocks*: [Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*

seq_lengths*: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]*

*property*shape*: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), ...]*

sparsity()[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L1446)

Computes the percentage of blocks that are sparse (i.e. not computed)

Return type:

[float](https://docs.python.org/3/library/functions.html#float)

to(*device*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L1540)

Moves the BlockMask to the specified device.

Parameters:

**device** ([*torch.device*](tensor_attributes.html#torch.device)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The target device to move the BlockMask to.
Can be a torch.device object or a string (e.g., 'cpu', 'cuda:0').

Returns:

A new BlockMask instance with all tensor components moved
to the specified device.

Return type:

BlockMask

Note

This method does not modify the original BlockMask in-place.
Instead, it returns a new BlockMask instance where individual tensor attributes
may or may not be moved to the specified device, depending on their
current device placement.

to_dense()[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L1459)

Returns a dense block that is equivalent to the block mask.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

to_string(*grid_size=(20, 20)*, *limit=4*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/nn/attention/flex_attention.py#L1475)

Returns a string representation of the block mask. Quite nifty.

If grid_size is -1, prints out an uncompressed version. Warning, it can be quite big!

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)