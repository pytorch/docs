# PerBlock

*class*torch.ao.quantization.observer.PerBlock(*block_size*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/ao/quantization/observer.py#L1699)

Represents per-block granularity in quantization. See
`quantize_affine()` for docs for
block_size

Variables:

**block_size** (*Tuple**[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**...**]*) - The size of each quantization group