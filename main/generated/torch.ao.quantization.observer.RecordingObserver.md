# RecordingObserver

*class*torch.ao.quantization.observer.RecordingObserver(*dtype=torch.quint8*)[[source]](https://github.com/pytorch/pytorch/blob/ca0571943b5289419bf52b30ee31769eb76a58c8/torch/ao/quantization/observer.py#L1540)

The module is mainly for debug and records the tensor values during runtime.

Parameters:

- **dtype** - Quantized data type
- **qscheme** - Quantization scheme to be used
- **reduce_range** - Reduces the range of the quantized data type by 1 bit