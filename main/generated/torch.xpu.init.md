# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/xpu/__init__.py#L331)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.