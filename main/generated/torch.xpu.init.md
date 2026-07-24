# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/xpu/__init__.py#L334)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.