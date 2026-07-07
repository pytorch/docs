# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/24e9a3928e16bb875a0a4ae3d26677dd7ddc8e02/torch/xpu/__init__.py#L334)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.