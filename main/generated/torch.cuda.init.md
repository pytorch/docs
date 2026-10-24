# torch.cuda.init

torch.cuda.init()[[source]](https://github.com/pytorch/pytorch/blob/9aee436a1bfc7a0bd2c40f48f128cb185ee3d75e/torch/cuda/__init__.py#L574)

Initialize PyTorch's CUDA state.

You may need to call this explicitly if you are interacting with
PyTorch via its C API, as Python bindings for CUDA functionality
will not be available until this initialization takes place.
Ordinary users should not need this, as all of PyTorch's CUDA methods
automatically initialize CUDA state on-demand.

Does nothing if the CUDA state is already initialized.