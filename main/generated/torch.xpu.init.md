# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/xpu/__init__.py#L360)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.