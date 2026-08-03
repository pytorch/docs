# get_block_size

*class*torch.ao.quantization.observer.get_block_size(*input_shape*, *granularity*)[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/ao/quantization/observer.py#L1790)

Get the block size based on the input shape and granularity type.

Parameters:

- **input_shape** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,**...**]*) - The input tensor shape possibly more than 2 dimensions
- **granularity** ([*Granularity*](torch.ao.quantization.observer.Granularity.html#torch.ao.quantization.observer.Granularity)) - The granularity type of the quantization

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), ...]