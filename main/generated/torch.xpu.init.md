# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/xpu/__init__.py#L333)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.