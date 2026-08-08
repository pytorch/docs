# RecordingObserver

*class*torch.ao.quantization.observer.RecordingObserver(*dtype=torch.quint8*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/ao/quantization/observer.py#L1540)

The module is mainly for debug and records the tensor values during runtime.

Parameters:

- **dtype** - Quantized data type
- **qscheme** - Quantization scheme to be used
- **reduce_range** - Reduces the range of the quantized data type by 1 bit