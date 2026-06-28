# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/xpu/__init__.py#L333)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.