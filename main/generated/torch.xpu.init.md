# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/xpu/__init__.py#L333)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.