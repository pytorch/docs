# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/xpu/__init__.py#L334)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.