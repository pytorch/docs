# PerRow

*class*torch.ao.quantization.observer.PerRow[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/ao/quantization/observer.py#L1787)

Represents row-wise granularity in quantization.

This is a special case of per-axis quantization and is unique to Float8 matmuls
where the input is quantized with a block_size of (1, ..., input.shape[-1]). And the weight
is quantized with a block_size of (1, weight.shape[1]).