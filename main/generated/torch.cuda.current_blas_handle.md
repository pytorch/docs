# torch.cuda.current_blas_handle

torch.cuda.current_blas_handle()[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/cuda/__init__.py#L1420)

Return the `cublasHandle_t` pointer for the current device and stream.

On CUDA, the handle uses cuBLAS's default workspace unless ATen workspace
caching is explicitly enabled. When caching is disabled, internal ATen
operations may temporarily bind their own workspace, but restore the default
workspace before releasing it. ROCm caches workspaces by default.