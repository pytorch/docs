# torch.xpu.init

torch.xpu.init()[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/xpu/__init__.py#L333)

Initialize PyTorch's XPU state.
This is a Python API about lazy initialization that avoids initializing
XPU until the first time it is accessed. Does nothing if the XPU state is
already initialized.