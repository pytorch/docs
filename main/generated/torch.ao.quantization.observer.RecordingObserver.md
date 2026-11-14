# RecordingObserver

*class*torch.ao.quantization.observer.RecordingObserver(*dtype=torch.quint8*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/ao/quantization/observer.py#L1563)

The module is mainly for debug and records the tensor values during runtime.

Parameters:

- **dtype** - Quantized data type
- **qscheme** - Quantization scheme to be used
- **reduce_range** - Reduces the range of the quantized data type by 1 bit