# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/xpu/__init__.py#L334)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.