# PerBlock

*class*torch.ao.quantization.observer.PerBlock(*block_size*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/ao/quantization/observer.py#L1722)

Represents per-block granularity in quantization. See
`quantize_affine()` for docs for
block_size

Variables:

**block_size** (*Tuple**[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**...**]*) - The size of each quantization group