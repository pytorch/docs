# torch.cuda.current_blas_handle

torch.cuda.current_blas_handle()[[source]](https://github.com/pytorch/pytorch/blob/e1994aea9ce307fb82feeb7524ab2c5d36771e4f/torch/cuda/__init__.py#L1420)

Return the `cublasHandle_t` pointer for the current device and stream.

On CUDA, the handle uses cuBLAS's default workspace unless ATen workspace
caching is explicitly enabled. When caching is disabled, internal ATen
operations may temporarily bind their own workspace, but restore the default
workspace before releasing it. ROCm caches workspaces by default.