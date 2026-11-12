# RecordingObserver

*class*torch.ao.quantization.observer.RecordingObserver(*dtype=torch.quint8*)[[source]](https://github.com/pytorch/pytorch/blob/c5a2c86d66eda12ed122b796baae9cb0aaf5aefb/torch/ao/quantization/observer.py#L1563)

The module is mainly for debug and records the tensor values during runtime.

Parameters:

- **dtype** - Quantized data type
- **qscheme** - Quantization scheme to be used
- **reduce_range** - Reduces the range of the quantized data type by 1 bit