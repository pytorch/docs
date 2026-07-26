# PerBlock

*class*torch.ao.quantization.observer.PerBlock(*block_size*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/ao/quantization/observer.py#L1699)

Represents per-block granularity in quantization. See
`quantize_affine()` for docs for
block_size

Variables:

**block_size** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,**...**]*) - The size of each quantization group