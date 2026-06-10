# PerRow

*class*torch.ao.quantization.observer.PerRow[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/ao/quantization/observer.py#L1764)

Represents row-wise granularity in quantization.

This is a special case of per-axis quantization and is unique to Float8 matmuls
where the input is quantized with a block_size of (1, ..., input.shape[-1]). And the weight
is quantized with a block_size of (1, weight.shape[1]).