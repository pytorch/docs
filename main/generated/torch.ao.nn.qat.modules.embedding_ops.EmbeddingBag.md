# EmbeddingBag

*class*torch.ao.nn.qat.modules.embedding_ops.EmbeddingBag(*num_embeddings*, *embedding_dim*, *max_norm=None*, *norm_type=2.0*, *scale_grad_by_freq=False*, *mode='mean'*, *sparse=False*, *_weight=None*, *include_last_offset=False*, *padding_idx=None*, *qconfig=None*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/fd6d216e3e8bf07c470716dfbf022d82fadd521d/torch/ao/nn/qat/modules/embedding_ops.py#L133)

An embedding bag module attached with FakeQuantize modules for weight,
used for quantization aware training.

We adopt the same interface as torch.nn.EmbeddingBag, please see
[https://pytorch.org/docs/stable/generated/torch.nn.EmbeddingBag.html#torch.nn.EmbeddingBag](https://pytorch.org/docs/stable/generated/torch.nn.EmbeddingBag.html#torch.nn.EmbeddingBag)
for documentation.

Similar to torch.nn.EmbeddingBag, with FakeQuantize modules initialized to
default.

Variables:

**weight** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - fake quant module for weight

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/fd6d216e3e8bf07c470716dfbf022d82fadd521d/torch/ao/nn/qat/modules/embedding_ops.py#L207)

Create a qat module from a float module

Args: mod a float module, either produced by torch.ao.quantization utilities
or directly from user