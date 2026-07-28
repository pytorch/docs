# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/b7ee7397ead012835c2d80ee53f64800630b1ab9/torch/xpu/__init__.py#L334)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.