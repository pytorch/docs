# PerRow

*class*torch.ao.quantization.observer.PerRow[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/ao/quantization/observer.py#L1787)

Represents row-wise granularity in quantization.

This is a special case of per-axis quantization and is unique to Float8 matmuls
where the input is quantized with a block_size of (1, ..., input.shape[-1]). And the weight
is quantized with a block_size of (1, weight.shape[1]).