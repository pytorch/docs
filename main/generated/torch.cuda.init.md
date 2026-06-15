# torch.cuda.init

torch.cuda.init()[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/cuda/__init__.py#L483)

Initialize PyTorch's CUDA state.

You may need to call this explicitly if you are interacting with
PyTorch via its C API, as Python bindings for CUDA functionality
will not be available until this initialization takes place.
Ordinary users should not need this, as all of PyTorch's CUDA methods
automatically initialize CUDA state on-demand.

Does nothing if the CUDA state is already initialized.