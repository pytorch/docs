# EmbeddingBag

*class*torch.ao.nn.quantized.EmbeddingBag(*num_embeddings*, *embedding_dim*, *max_norm=None*, *norm_type=2.0*, *scale_grad_by_freq=False*, *mode='sum'*, *sparse=False*, *_weight=None*, *include_last_offset=False*, *dtype=torch.quint8*)[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/ao/nn/quantized/modules/embedding_ops.py#L268)

A quantized EmbeddingBag module with quantized packed weights as inputs.
We adopt the same interface as torch.nn.EmbeddingBag, please see
[https://pytorch.org/docs/stable/generated/torch.nn.EmbeddingBag.html](https://pytorch.org/docs/stable/generated/torch.nn.EmbeddingBag.html) for documentation.

Similar to [`EmbeddingBag`](torch.nn.EmbeddingBag.html#torch.nn.EmbeddingBag), attributes will be randomly
initialized at module creation time and will be overwritten later

Variables:

**weight** ([*Tensor*](../tensors.html#torch.Tensor)) - the non-learnable quantized weights of the module of
shape (num_embeddings,embedding_dim)(\text{num\_embeddings}, \text{embedding\_dim})(num_embeddings,embedding_dim).

Examples::

```
>>> m = nn.quantized.EmbeddingBag(num_embeddings=10, embedding_dim=12, include_last_offset=True, mode='sum')
>>> indices = torch.tensor([9, 6, 5, 7, 8, 8, 9, 2, 8, 6, 6, 9, 1, 6, 8, 8, 3, 2, 3, 6, 3, 6, 5, 7, 0, 8, 4, 6, 5, 8, 2, 3])
>>> offsets = torch.tensor([0, 19, 20, 28, 28, 32])
>>> output = m(indices, offsets)
>>> print(output.size())
torch.Size([5, 12])
```

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/ao/nn/quantized/modules/embedding_ops.py#L348)

Create a quantized embedding_bag module from a float module

Parameters:

**mod** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - a float module, either produced by torch.ao.quantization
utilities or provided by user