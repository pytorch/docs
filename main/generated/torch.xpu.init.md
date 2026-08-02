# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/xpu/__init__.py#L334)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.