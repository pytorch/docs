# PerBlock

*class*torch.ao.quantization.observer.PerBlock(*block_size*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/quantization/observer.py#L1699)

Represents per-block granularity in quantization. See
`quantize_affine()` for docs for
block_size

Variables:

**block_size** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,**...**]*) - The size of each quantization group