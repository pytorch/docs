# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/99fcf9fd884002c14d4c19cce5dfe2469ba5a7fc/torch/xpu/__init__.py#L334)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.