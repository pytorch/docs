# get_block_size

*class*torch.ao.quantization.observer.get_block_size(*input_shape*, *granularity*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/ao/quantization/observer.py#L1790)

Get the block size based on the input shape and granularity type.

Parameters:

- **input_shape** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,**...**]*) - The input tensor shape possibly more than 2 dimensions
- **granularity** ([*Granularity*](torch.ao.quantization.observer.Granularity.html#torch.ao.quantization.observer.Granularity)) - The granularity type of the quantization

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), ...]