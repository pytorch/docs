# torch.cuda.init

torch.cuda.init()[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/cuda/__init__.py#L549)

Initialize PyTorch's CUDA state.

You may need to call this explicitly if you are interacting with
PyTorch via its C API, as Python bindings for CUDA functionality
will not be available until this initialization takes place.
Ordinary users should not need this, as all of PyTorch's CUDA methods
automatically initialize CUDA state on-demand.

Does nothing if the CUDA state is already initialized.