# torch.onnx.ops

ONNX operators as native torch.fx operators.

This module provides a set of functions to create ONNX operators in the FX graph
which are exportable to ONNX.

## Symbolic Operators

Operators that can be used to create any ONNX ops in the FX graph symbolically.
These operators do not do actual computation. It's recommended that you used them
inside an `if torch.onnx.is_in_onnx_export` block.

torch.onnx.ops.symbolic(*domain_op*, */*, *inputs*, *attrs=None*, ***, *dtype*, *shape*, *version=None*, *metadata_props=None*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/onnx/ops/__init__.py#L73)

Create a symbolic FX operator to represent an arbitrary ONNX operator.

This function is used to create a symbolic operator with a single output.
To create an operator with multiple outputs, use `symbolic_multi_out()`.

You may use `if torch.onnx.is_in_onnx_export()` to conditionally enable the
symbolic logic only during `torch.onnx.export()`.

Example:

```
class CustomOp(torch.nn.Module):
 def forward(self, x: torch.Tensor) -> torch.Tensor:
 # Normal torch operators can interleave with the symbolic ops during ONNX export
 x = x + 1

 # Create a symbolic ONNX operator with the name "CustomOp" in the "custom_domain" domain.
 # The output tensor will have the specified dtype and shape
 val = torch.onnx.ops.symbolic(
 "custom_domain::CustomOp",
 (x,),
 dict(attr_key="attr_value"),
 dtype=x.dtype,
 shape=x.shape,
 version=1,
 )

 # The result of the symbolic op can be used in normal torch operations during ONNX export
 return torch.nn.functional.relu(val)

# You may then export this model to ONNX using torch.onnx.export(..., dynamo=True).
```

Parameters:

- **domain_op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The domain and operator name, separated by "::". For example,
"custom_domain::CustomOp".
- **inputs** (*Sequence**[*[*torch.Tensor*](tensors.html#torch.Tensor)*|**None**]*) - The input tensors to the operator.
- **attrs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*|*[*float*](https://docs.python.org/3/library/functions.html#float)*|*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*bool*](https://docs.python.org/3/library/functions.html#bool)*|**Sequence**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**|**Sequence**[*[*float*](https://docs.python.org/3/library/functions.html#float)*]**|**Sequence**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**Sequence**[*[*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]**|**None*) - The attributes of the operator. The keys are attribute names and
the values are attribute values. Valid attribute types are int, float,
str, bool, and lists of int, float, str, and bool. Tensor attributes
are unsupported.
- **dtype** ([*torch.dtype*](tensor_attributes.html#torch.dtype)*|*[*int*](https://docs.python.org/3/library/functions.html#int)) - The data type of the output tensor.This can be either a torch.dtype
or an integer representing the ONNX data type.
- **shape** (*Sequence**[*[*int*](https://docs.python.org/3/library/functions.html#int)*|*[*torch.SymInt*](torch.html#torch.SymInt)*]*) - The shape of the output tensor. This can be a list of integers or
SymInt values.
- **version** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None*) - The version of the opset used for the operator.
- **metadata_props** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**None*) - Metadata properties for the ONNX node.
This is a dictionary of str-str pairs.

Returns:

The output tensor of the operator.

Return type:

[torch.Tensor](tensors.html#torch.Tensor)

torch.onnx.ops.symbolic_multi_out(*domain_op*, */*, *inputs*, *attrs=None*, ***, *dtypes*, *shapes*, *version=None*, *metadata_props=None*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/onnx/ops/__init__.py#L174)

Create a symbolic FX operator to represent an arbitrary ONNX operator with multiple outputs.

You may use `if torch.onnx.is_in_onnx_export()` to conditionally enable the
symbolic logic only during `torch.onnx.export()`.

Example:

```
class CustomOp(torch.nn.Module):
 def forward(self, x: torch.Tensor) -> torch.Tensor:
 # Normal torch operators can interleave with the symbolic ops during ONNX export
 x = x + 1

 # Create a symbolic ONNX operator with the name "CustomOp" in the "custom_domain" domain.
 # The output tensors will have the specified dtypes and shapes
 (out1, out2) = torch.onnx.ops.symbolic_multi_out(
 "custom_domain::CustomOp",
 (x,),
 dict(attr_key="attr_value"),
 dtypes=(x.dtype, torch.float32),
 shapes=(x.shape, [1, 2, 3]),
 version=1,
 )

 # The result of the symbolic op can be used in normal torch operations during ONNX export
 return torch.nn.functional.relu(out1 + out2)

# You may then export this model to ONNX using torch.onnx.export(..., dynamo=True).
```

Parameters:

- **domain_op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The domain and operator name, separated by "::". For example,
"custom_domain::CustomOp".
- **inputs** (*Sequence**[*[*torch.Tensor*](tensors.html#torch.Tensor)*|**None**]*) - The input tensors to the operator.
- **attrs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*|*[*float*](https://docs.python.org/3/library/functions.html#float)*|*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*bool*](https://docs.python.org/3/library/functions.html#bool)*|**Sequence**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**|**Sequence**[*[*float*](https://docs.python.org/3/library/functions.html#float)*]**|**Sequence**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**Sequence**[*[*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]**|**None*) - The attributes of the operator. The keys are attribute names and
the values are attribute values. Valid attribute types are int, float,
str, bool, and lists of int, float, str, and bool. Tensor attributes
are unsupported.
- **dtypes** (*Sequence**[*[*torch.dtype*](tensor_attributes.html#torch.dtype)*|*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - The data types of the output tensors. This can be a list of
torch.dtype or integers representing the ONNX data types. The length
of this list must be the number of outputs.
- **shapes** (*Sequence**[**Sequence**[*[*int*](https://docs.python.org/3/library/functions.html#int)*|*[*torch.SymInt*](torch.html#torch.SymInt)*]**]*) - The shapes of the output tensors. This can be a list of lists of
integers or SymInt values. The length of this list must be the number of outputs.
- **version** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None*) - The version of the opset used for the operator.
- **metadata_props** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**None*) - Metadata properties for the ONNX node.
This is a dictionary of str-str pairs.

Returns:

A list of output tensors of the operator.

Return type:

Sequence[[torch.Tensor](tensors.html#torch.Tensor)]

## ONNX Operators

The following operators are implemented as native PyTorch ops and can be exported as
ONNX operators. They can be used natively in an `nn.Module`.

For example, you can define a module:

```
class Model(torch.nn.Module):
 def forward(
 self, input_data, cos_cache_data, sin_cache_data, position_ids_data
 ):
 return torch.onnx.ops.rotary_embedding(
 input_data,
 cos_cache_data,
 sin_cache_data,
 position_ids_data,
 )
```

and export it to ONNX using:

```
input_data = torch.rand(2, 3, 4, 8)
position_ids_data = torch.randint(0, 50, (2, 3)).long()
sin_cache_data = torch.rand(50, 4)
cos_cache_data = torch.rand(50, 4)
dynamic_shapes = {
 "input_data": {0: torch.export.Dim.DYNAMIC},
 "cos_cache_data": None,
 "sin_cache_data": None,
 "position_ids_data": {0: torch.export.Dim.DYNAMIC},
}
onnx_program = torch.onnx.export(
 model,
 (input_data, cos_cache_data, sin_cache_data, position_ids_data),
 dynamic_shapes=dynamic_shapes,
 dynamo=True,
 opset_version=23,
)
```

Printing the ONNX program will show the ONNX operators used in the graph:

```
<...>

graph(
 name=main_graph,
 inputs=(
 %"input_data"<FLOAT,[s0,3,4,8]>,
 %"cos_cache_data"<FLOAT,[50,4]>,
 %"sin_cache_data"<FLOAT,[50,4]>,
 %"position_ids_data"<INT64,[s0,3]>
 ),
 outputs=(
 %"rotary_embedding"<FLOAT,[s0,3,4,8]>
 ),
) {
 0 | # rotary_embedding
 %"rotary_embedding"<FLOAT,[s0,3,4,8]> ⬅️ ::RotaryEmbedding(%"input_data", %"cos_cache_data", %"sin_cache_data", %"position_ids_data")
 return %"rotary_embedding"<FLOAT,[s0,3,4,8]>
}
```

with the corresponding `ExportedProgram`:

ExportedProgram:

```
class GraphModule(torch.nn.Module):
 def forward(self, input_data: "f32[s0, 3, 4, 8]", cos_cache_data: "f32[50, 4]", sin_cache_data: "f32[50, 4]", position_ids_data: "i64[s0, 3]"):
 rotary_embedding: "f32[s0, 3, 4, 8]" = torch.ops.onnx.RotaryEmbedding.opset23(input_data, cos_cache_data, sin_cache_data, position_ids_data); input_data = cos_cache_data = sin_cache_data = position_ids_data = None
 return (rotary_embedding,)
```

torch.onnx.ops.rotary_embedding(*X*, *cos_cache*, *sin_cache*, *position_ids=None*, ***, *interleaved=False*, *num_heads=0*, *rotary_embedding_dim=0*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/onnx/ops/__init__.py#L282)

RotaryEmbedding op in ONNX.

[https://onnx.ai/onnx/operators/onnx__RotaryEmbedding.html](https://onnx.ai/onnx/operators/onnx__RotaryEmbedding.html)

RotaryEmbedding is the implementation of rotary positional embeddings (RoPE) based on the paper [https://arxiv.org/pdf/2104.09864](https://arxiv.org/pdf/2104.09864).
The key advantage of RoPE is that it allows the model to understand both the absolute position of a token and the relative distances
between tokens. This is achieved through a rotational mechanism where the extent of rotation is computed based on the token's absolute position (position_ids).

The rotational mechanism is defined by sine and cosine functions that are used to represent the rotation angles.
For each token in the sequence, its positional embedding is computed by rotating its embedding vector. This is done by splitting the
embedding vector either into two halves or interleaving every alternate token and applying the rotation matrix to each half of the embedding vector.
The rotation matrix is parameterized by the token's position in the sequence. The rotated halves of the embedding vector are concatenated
to form the final positional embedding for each token. The rotated positional embeddings are used in the self-attention mechanism.
The rotation ensures that the model captures both absolute and relative positional information.

Parameters:

- **X** ([*Tensor*](tensors.html#torch.Tensor)) - The input tensor representing the token embeddings. 4D tensor with
shape (batch_size, num_heads, sequence_length, head_size) or 3D tensor
with shape (batch_size, sequence_length, hidden_size). For cases with
a 4D input tensor, head_size has to be even. For cases with a 3D input
tensor, num_heads attribute must be provided and hidden_size must
be an even multiple of num_heads where hidden_size = num_heads * head_size
- **cos_cache** ([*Tensor*](tensors.html#torch.Tensor)) - The cosine values for the rotation. 2D tensor with shape (max_position_id_plus_1, head_size / 2)
for full rotation or (max_position_id_plus_1, rotary_embedding_dim / 2)
for partial rotation when position_ids are provided. 3D tensor with shape
(batch_size, sequence_length, head_size / 2) for full rotation or
(batch_size, sequence_length, rotary_embedding_dim / 2) for partial
rotation when position_ids are not provided. max_position_id_plus_1
is a parameter to the model.
- **sin_cache** ([*Tensor*](tensors.html#torch.Tensor)) - The sine values for the rotation. 2D tensor with shape (max_position_id_plus_1, head_size / 2)
for full rotation or (max_position_id_plus_1, rotary_embedding_dim / 2)
for partial rotation when position_ids are provided. 3D tensor with shape
(batch_size, sequence_length, head_size / 2) for full rotation or
(batch_size, sequence_length, rotary_embedding_dim / 2) for partial rotation
when position_ids are not provided. max_position_id_plus_1 is a parameter
to the model.
- **position_ids** ([*Tensor*](tensors.html#torch.Tensor)*|**None*) - The position indices for the tokens. 2D tensor with shape
(batch_size, sequence_length).
- **interleaved** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Rotate using interleaved pattern. Default value is 0 (False).
- **num_heads** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of attention heads. Must be provided when input is a 3D tensor.
- **rotary_embedding_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Rotary embedding dimension used to apply partial rotary embeddings.

Returns:

Tensor with same shape as input.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

torch.onnx.ops.attention(*Q*, *K*, *V*, *attn_mask=None*, *past_key=None*, *past_value=None*, ***, *is_causal=False*, *kv_num_heads=0*, *q_num_heads=0*, *qk_matmul_output_mode=0*, *scale=None*, *softcap=0.0*, *softmax_precision=None*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/onnx/ops/__init__.py#L348)

Attention op in ONNX.

[https://onnx.ai/onnx/operators/onnx__Attention.html](https://onnx.ai/onnx/operators/onnx__Attention.html)

Computes scaled dot product attention on query, key and value tensors, using an optional attention mask if passed.

This operator covers self and cross variants of the attention operation based on sequence lengths of K, Q and V.

For self attention, `kv_sequence_length` equals to `q_sequence_length`.

For cross attention, query and key might have different lengths.

This operator also covers the 3 following variants based on the number of heads:

1. Multi-headed Attention (MHA): Described in the paper [https://arxiv.org/pdf/1706.03762](https://arxiv.org/pdf/1706.03762), q_num_heads = kv_num_heads.
2. Group-query Attention (GQA): Described in the paper [https://arxiv.org/pdf/2305.13245](https://arxiv.org/pdf/2305.13245), q_num_heads > kv_num_heads, q_num_heads % kv_num_heads == 0.
3. Multi-query Attention (MQA): Described in the paper [https://arxiv.org/pdf/1911.02150](https://arxiv.org/pdf/1911.02150), q_num_heads > kv_num_heads, kv_num_heads=1.

Attention bias to be added is calculated based on `attn_mask` input and is_causal` `attribute, only one of which can be provided.

1. If `is_causal` is set to 1, the attention masking is a lower triangular matrix when the mask is a square matrix. The attention masking has the form of the upper left causal bias due to the alignment.
2. attn_mask: A boolean mask where a value of True indicates that the element should take part in attention or a float mask of the same type as query, key, value that is added to the attention score.

Both past and present state key/values are optional. They shall be used together, and not allowed to use only one of them.
The following pattern is applied to the Q, K and V inputs after appropriate reshaping of K and V inputs based on sequence lengths and num heads provided:

```
The following pattern is applied by this operator:
 Q K V
 | | |
Q*sqrt(scale) K*sqrt(scale) |
 | | |
 | Transpose |
 | | |
 ---MatMul--- |
 | |
at_mask---Add |
 | |
 softcap (if provided) |
 | |
 Softmax |
 | |
 -----MatMul------
 |
 Y
```

Parameters:

- **Q** ([*Tensor*](tensors.html#torch.Tensor)) - Query tensor. 4D tensor with shape (batch_size, q_num_heads, q_sequence_length, head_size) or 3D tensor
with shape (batch_size, q_sequence_length, q_hidden_size). For cases with a 3D input tensor,
q_hidden_size = q_num_heads * head_size
- **K** ([*Tensor*](tensors.html#torch.Tensor)) - Key tensor. 4D tensor with shape (batch_size, kv_num_heads, kv_sequence_length, head_size) or 3D tensor
with shape (batch_size, kv_sequence_length, k_hidden_size). For cases with a 3D input tensor,
k_hidden_size = kv_num_heads * head_size
- **V** ([*Tensor*](tensors.html#torch.Tensor)) - Value tensor. 4D tensor with shape (batch_size, kv_num_heads, kv_sequence_length, v_head_size) or 3D tensor
with shape (batch_size, kv_sequence_length, v_hidden_size). For cases with a 3D input tensor,
v_hidden_size = kv_num_heads * v_head_size
- **attn_mask** ([*Tensor*](tensors.html#torch.Tensor)*|**None*) - Attention mask. Shape must be broadcastable to 4D tensor with shape
(batch_size, q_num_heads, q_sequence_length, total_sequence_length) where
total_sequence_length = past_sequence_length + kv_sequence_length. Two types of masks are supported.
A boolean mask where a value of True indicates that the element should take part in attention.
Also supports a float mask of the same type as query, key, value that is added to the attention score.
- **past_key** ([*Tensor*](tensors.html#torch.Tensor)*|**None*) - Past state cache for key with shape (batch_size, kv_num_heads, past_sequence_length, head_size)
- **past_value** ([*Tensor*](tensors.html#torch.Tensor)*|**None*) - Past state cache for value with shape (batch_size, kv_num_heads, past_sequence_length, v_head_size)
- **is_causal** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to True, the attention masking is a lower triangular matrix when the mask is a square matrix.
The attention masking has the form of the upper left causal bias due to the alignment.
- **kv_num_heads** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of heads of key and value. Must be used with 3D inputs of Q, K and V.
- **q_num_heads** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of heads of query. Must be used with 3D inputs of Q, K and V.
- **qk_matmul_output_mode** ([*int*](https://docs.python.org/3/library/functions.html#int)) - If set to 0, qk_matmul_output is the output of qk matmul. If set to 1,
qk_matmul_output includes the addition of the attention mask to the output of qk matmul.
If set to 2, qk_matmul_output is the output after the softcap operation. If set to 3,
qk_matmul_output is the output after the softmax operation. Default value is 0.
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*|**None*) - Scaling factor applied to Q*K^T. Default value is 1/sqrt(head_size). To prevent numerical overflow,
scale Q, K by sqrt(scale) before matmul.
- **softcap** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Softcap value for attention weights. Default value is 0.
- **softmax_precision** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None*) - The floating-point precision used in softmax computation. If softmax precision is not provided,
the same precision as the input of softmax (Q and K) is used.

Returns:

- The output tensor. 4D tensor with shape (batch_size, q_num_heads, q_sequence_length, v_head_size) or 3D tensor
with shape (batch_size, q_sequence_length, hidden_size). For cases with a 3D input tensor,
hidden_size = q_num_heads * v_head_size
- Updated key cache with shape (batch_size, kv_num_heads, total_sequence_length, head_size) where
total_sequence_length = past_sequence_length + kv_sequence_length.
- Updated value cache with shape (batch_size, kv_num_heads, total_sequence_length, v_head_size) where
total_sequence_length = past_sequence_length + kv_sequence_length.
- The output of QK matmul. 4D tensor with shape (batch_size, q_num_heads, q_sequence_length, total_sequence_length)
where total_sequence_length = past_sequence_length + kv_sequence_length.

Return type:

A tuple containing

## ONNX to ATen Decomposition Table

You can use `torch.onnx.ops.aten_decompositions()` to obtain a decomposition table
to decompose ONNX operators defined above to ATen operators.

```
class Model(torch.nn.Module):
 def forward(
 self, input_data, cos_cache_data, sin_cache_data, position_ids_data
 ):
 return torch.onnx.ops.rotary_embedding(
 input_data,
 cos_cache_data,
 sin_cache_data,
 position_ids_data,
 )

model = Model()

ep = torch.export.export(
 model,
 (input_data, cos_cache_data, sin_cache_data, position_ids_data),
)
# The program can be decomposed into aten ops
ep_decomposed = ep.run_decompositions(torch.onnx.ops.aten_decompositions())
```

torch.onnx.ops.aten_decompositions()[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/onnx/ops/__init__.py#L57)

Return the ONNX to ATen decomp table.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[torch._ops.OpOverload, Callable]