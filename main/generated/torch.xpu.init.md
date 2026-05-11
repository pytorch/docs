# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/xpu/__init__.py#L327)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.