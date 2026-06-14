# Embedding

*class*torch.ao.nn.qat.modules.embedding_ops.Embedding(*num_embeddings*, *embedding_dim*, *padding_idx=None*, *max_norm=None*, *norm_type=2.0*, *scale_grad_by_freq=False*, *sparse=False*, *_weight=None*, *device=None*, *dtype=None*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/40e21dcd4b92d59842b3e3b7f542f855dedddb91/torch/ao/nn/qat/modules/embedding_ops.py#L11)

An embedding bag module attached with FakeQuantize modules for weight,
used for quantization aware training.

We adopt the same interface as torch.nn.Embedding, please see
[https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html#torch.nn.Embedding](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html#torch.nn.Embedding)
for documentation.

Similar to torch.nn.Embedding, with FakeQuantize modules initialized to
default.

Variables:

**weight** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - fake quant module for weight

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/40e21dcd4b92d59842b3e3b7f542f855dedddb91/torch/ao/nn/qat/modules/embedding_ops.py#L77)

Create a qat module from a float module

Args: mod a float module, either produced by torch.ao.quantization utilities
or directly from user