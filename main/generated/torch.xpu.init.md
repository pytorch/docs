# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/xpu/__init__.py#L333)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.