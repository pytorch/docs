# PerBlock

*class*torch.ao.quantization.observer.PerBlock(*block_size*)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/ao/quantization/observer.py#L1699)

Represents per-block granularity in quantization. See
`quantize_affine()` for docs for
block_size

Variables:

**block_size** (*Tuple**[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**...**]*) - The size of each quantization group