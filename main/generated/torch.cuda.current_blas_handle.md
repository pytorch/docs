# torch.cuda.current_blas_handle

torch.cuda.current_blas_handle()[[source]](https://github.com/pytorch/pytorch/blob/c712ec6ebb4ecd2838e2cafb0bbc7a3c5acfe668/torch/cuda/__init__.py#L1420)

Return the `cublasHandle_t` pointer for the current device and stream.

On CUDA, the handle uses cuBLAS's default workspace unless ATen workspace
caching is explicitly enabled. When caching is disabled, internal ATen
operations may temporarily bind their own workspace, but restore the default
workspace before releasing it. ROCm caches workspaces by default.