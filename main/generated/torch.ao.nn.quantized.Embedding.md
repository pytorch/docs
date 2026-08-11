# Embedding

*class*torch.ao.nn.quantized.Embedding(*num_embeddings*, *embedding_dim*, *padding_idx=None*, *max_norm=None*, *norm_type=2.0*, *scale_grad_by_freq=False*, *sparse=False*, *_weight=None*, *dtype=torch.quint8*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/ao/nn/quantized/modules/embedding_ops.py#L97)

A quantized Embedding module with quantized packed weights as inputs.
We adopt the same interface as torch.nn.Embedding, please see
[https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html) for documentation.

Similar to [`Embedding`](torch.nn.Embedding.html#torch.nn.Embedding), attributes will be randomly
initialized at module creation time and will be overwritten later

Variables:

**weight** ([*Tensor*](../tensors.html#torch.Tensor)) - the non-learnable quantized weights of the module of
shape (num_embeddings,embedding_dim)(\text{num\_embeddings}, \text{embedding\_dim})(num_embeddings,embedding_dim).

Examples::

```
>>> m = nn.quantized.Embedding(num_embeddings=10, embedding_dim=12)
>>> indices = torch.tensor([9, 6, 5, 7, 8, 8, 9, 2, 8])
>>> output = m(indices)
>>> print(output.size())
torch.Size([9, 12])
```

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/ao/nn/quantized/modules/embedding_ops.py#L193)

Create a quantized embedding module from a float module

Parameters:

**mod** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - a float module, either produced by torch.ao.quantization
utilities or provided by user