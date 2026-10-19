# torch.cuda.init

torch.cuda.init()[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/__init__.py#L574)

Initialize PyTorch's CUDA state.

You may need to call this explicitly if you are interacting with
PyTorch via its C API, as Python bindings for CUDA functionality
will not be available until this initialization takes place.
Ordinary users should not need this, as all of PyTorch's CUDA methods
automatically initialize CUDA state on-demand.

Does nothing if the CUDA state is already initialized.