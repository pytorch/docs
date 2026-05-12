# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/xpu/__init__.py#L327)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.