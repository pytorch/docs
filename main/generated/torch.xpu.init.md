# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/xpu/__init__.py#L327)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.