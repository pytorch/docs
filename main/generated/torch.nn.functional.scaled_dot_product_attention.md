# torch.nn.functional.scaled_dot_product_attention

torch.nn.functional.scaled_dot_product_attention()[[source]](https://github.com/pytorch/pytorch/blob/ca0571943b5289419bf52b30ee31769eb76a58c8/torch/nn/functional.py#L6341)

scaled_dot_product_attention(query, key, value, attn_mask=None, dropout_p=0.0,

is_causal=False, scale=None, enable_gqa=False) -> Tensor:

Computes scaled dot product attention on query, key and value tensors, using an optional attention mask if passed,
and applying dropout if a probability greater than 0.0 is specified. The optional scale argument can only be
specified as a keyword argument.

```
# Efficient implementation equivalent to the following:
def scaled_dot_product_attention(query, key, value, attn_mask=None, dropout_p=0.0,
 is_causal=False, scale=None, enable_gqa=False) -> torch.Tensor:
 L, S = query.size(-2), key.size(-2)
 scale_factor = 1 / math.sqrt(query.size(-1)) if scale is None else scale
 attn_bias = torch.zeros(L, S, dtype=query.dtype, device=query.device)
 if is_causal:
 assert attn_mask is None
 temp_mask = torch.ones(L, S, dtype=torch.bool, device=query.device).tril(diagonal=0)
 attn_bias.masked_fill_(temp_mask.logical_not(), float("-inf"))

 if attn_mask is not None:
 if attn_mask.dtype == torch.bool:
 attn_bias.masked_fill_(attn_mask.logical_not(), float("-inf"))
 else:
 attn_bias = attn_mask + attn_bias

 if enable_gqa:
 key = key.repeat_interleave(query.size(-3)//key.size(-3), -3)
 value = value.repeat_interleave(query.size(-3)//value.size(-3), -3)

 attn_weight = query @ key.transpose(-2, -1) * scale_factor
 attn_weight += attn_bias
 attn_weight = torch.softmax(attn_weight, dim=-1)
 attn_weight = torch.dropout(attn_weight, dropout_p, train=True)
 return attn_weight @ value
```

Warning

This function is beta and subject to change.

Warning

This function always applies dropout according to the specified `dropout_p` argument.
To disable dropout during evaluation, be sure to pass a value of `0.0` when the module
that makes the function call is not in training mode.

For example:

```
class MyModel(nn.Module):
 def __init__(self, p=0.5):
 super().__init__()
 self.p = p

 def forward(self, ...):
 return F.scaled_dot_product_attention(...,
 dropout_p=(self.p if self.training else 0.0))
```

Note

The boolean mask semantics for `attn_mask` are the inverse of
[`MultiheadAttention`](torch.nn.MultiheadAttention.html#torch.nn.MultiheadAttention)'s `key_padding_mask`.

In `scaled_dot_product_attention()`, `True` indicates values
to **participate** in attention.

In [`MultiheadAttention`](torch.nn.MultiheadAttention.html#torch.nn.MultiheadAttention), `True` indicates values
to be **masked out** (padding).

If migrating from MHA, ensure you invert your boolean mask (e.g.,
using `~mask` or `mask.logical_not()`).

Note

There are currently three supported implementations of scaled dot product attention:

> - [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691)
> - [Memory-Efficient Attention](https://github.com/facebookresearch/xformers)
> - A PyTorch implementation defined in C++ matching the above formulation

The function may call optimized kernels for improved performance when using the CUDA backend.
For all other backends, the PyTorch implementation will be used.

All implementations are enabled by default. Scaled dot product attention attempts to automatically select the
most optimal implementation based on the inputs. In order to provide more fine-grained control over what implementation
is used, the following functions are provided for enabling and disabling implementations.
The context manager is the preferred mechanism:

> - [`torch.nn.attention.sdpa_kernel()`](torch.nn.attention.sdpa_kernel.html#torch.nn.attention.sdpa_kernel): A context manager used to enable or disable any of the implementations.
> - [`torch.backends.cuda.enable_flash_sdp()`](../backends.html#torch.backends.cuda.enable_flash_sdp): Globally enables or disables FlashAttention.
> - [`torch.backends.cuda.enable_mem_efficient_sdp()`](../backends.html#torch.backends.cuda.enable_mem_efficient_sdp): Globally enables or disables Memory-Efficient Attention.
> - [`torch.backends.cuda.enable_math_sdp()`](../backends.html#torch.backends.cuda.enable_math_sdp): Globally enables or disables the PyTorch C++ implementation.

Each of the fused kernels has specific input limitations. If the user requires the use of a specific fused implementation,
disable the PyTorch C++ implementation using [`torch.nn.attention.sdpa_kernel()`](torch.nn.attention.sdpa_kernel.html#torch.nn.attention.sdpa_kernel).
In the event that a fused implementation is not available, a warning will be raised with the
reasons why the fused implementation cannot run.

Due to the nature of fusing floating point operations, the output of this function may be different
depending on what backend kernel is chosen.
The c++ implementation supports torch.float64 and can be used when higher precision is required.
For math backend, all intermediates are kept in torch.float if inputs are in torch.half or torch.bfloat16.

For more information please see [Numerical accuracy](../notes/numerical_accuracy.html)

> Grouped Query Attention (GQA) is an experimental feature. It currently works only for Flash_attention
> and math kernel on CUDA tensor, and does not support Nested tensor.
> Constraints for GQA:
> 
> 
> 
> 
> > - number_of_heads_query % number_of_heads_key_value == 0 and,
> > - number_of_heads_key == number_of_heads_value

Note

In some circumstances when given tensors on a CUDA device and using CuDNN, this operator may select a nondeterministic algorithm to increase performance. If this is undesirable, you can try to make the operation deterministic (potentially at a performance cost) by setting `torch.backends.cudnn.deterministic = True`. See [Reproducibility](../notes/randomness.html) for more information.

Parameters:

- **query** ([*Tensor*](../tensors.html#torch.Tensor)) - Query tensor; shape (N,...,Hq,L,E)(N, ..., Hq, L, E)(N,...,Hq,L,E).
- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - Key tensor; shape (N,...,H,S,E)(N, ..., H, S, E)(N,...,H,S,E).
- **value** ([*Tensor*](../tensors.html#torch.Tensor)) - Value tensor; shape (N,...,H,S,Ev)(N, ..., H, S, Ev)(N,...,H,S,Ev).
- **attn_mask** (*optional Tensor*) - Attention mask; shape must be broadcastable to the shape of attention weights,
which is (N,...,Hq,L,S)(N,..., Hq, L, S)(N,...,Hq,L,S). Two types of masks are supported.
A boolean mask where a value of True indicates that the element *should* take part in attention.
A float mask of the same type as query, key, value that is added to the attention score.
- **dropout_p** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Dropout probability; if greater than 0.0, dropout is applied
- **is_causal** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to true, the attention masking is a lower triangular matrix when the mask is a
square matrix. The attention masking has the form of the upper left causal bias due to the alignment
(see [`torch.nn.attention.bias.CausalBias`](torch.nn.attention.bias.CausalBias.html#torch.nn.attention.bias.CausalBias)) when the mask is a non-square matrix.
An error is thrown if both attn_mask and is_causal are set.
- **scale** (*optional python:float**,**keyword-only*) - Scaling factor applied prior to softmax. If None, the default value is set
to 1E\frac{1}{\sqrt{E}}E​1​.
- **enable_gqa** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to True, Grouped Query Attention (GQA) is enabled, by default it is set to False.

Returns:

Attention output; shape (N,...,Hq,L,Ev)(N, ..., Hq, L, Ev)(N,...,Hq,L,Ev).

Return type:

output ([Tensor](../tensors.html#torch.Tensor))

Shape legend:

- N:Batch size...:Any number of other batch dimensions (optional)N: \text{Batch size} ... : \text{Any number of other batch dimensions (optional)}N:Batch size...:Any number of other batch dimensions (optional)
- S:Source sequence lengthS: \text{Source sequence length}S:Source sequence length
- L:Target sequence lengthL: \text{Target sequence length}L:Target sequence length
- E:Embedding dimension of the query and keyE: \text{Embedding dimension of the query and key}E:Embedding dimension of the query and key
- Ev:Embedding dimension of the valueEv: \text{Embedding dimension of the value}Ev:Embedding dimension of the value
- Hq:Number of heads of queryHq: \text{Number of heads of query}Hq:Number of heads of query
- H:Number of heads of key and valueH: \text{Number of heads of key and value}H:Number of heads of key and value

Examples

```
>>> # Optionally use the context manager to ensure one of the fused kernels is run
>>> query = torch.rand(32, 8, 128, 64, dtype=torch.float16, device="cuda")
>>> key = torch.rand(32, 8, 128, 64, dtype=torch.float16, device="cuda")
>>> value = torch.rand(32, 8, 128, 64, dtype=torch.float16, device="cuda")
>>> with sdpa_kernel(backends=[SDPBackend.FLASH_ATTENTION]):
>>> F.scaled_dot_product_attention(query,key,value)
```

```
>>> # Sample for GQA for llama3
>>> query = torch.rand(32, 32, 128, 64, dtype=torch.float16, device="cuda")
>>> key = torch.rand(32, 8, 128, 64, dtype=torch.float16, device="cuda")
>>> value = torch.rand(32, 8, 128, 64, dtype=torch.float16, device="cuda")
>>> with sdpa_kernel(backends=[SDPBackend.MATH]):
>>> F.scaled_dot_product_attention(query,key,value,enable_gqa=True)
```