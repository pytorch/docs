# RecordingObserver

*class*torch.ao.quantization.observer.RecordingObserver(*dtype=torch.quint8*)[[source]](https://github.com/pytorch/pytorch/blob/e97ee94e32f26ccec33db4c1411bddc4cc9e1a31/torch/ao/quantization/observer.py#L1541)

The module is mainly for debug and records the tensor values during runtime.

Parameters:

- **dtype** - Quantized data type
- **qscheme** - Quantization scheme to be used
- **reduce_range** - Reduces the range of the quantized data type by 1 bit