# torch.cuda.current_blas_handle

torch.cuda.current_blas_handle()[[source]](https://github.com/pytorch/pytorch/blob/50d50e722913b05a0762c886507c9be7ae43d2f3/torch/cuda/__init__.py#L1459)

Return the `cublasHandle_t` pointer for the current device and stream.

On CUDA, the handle uses the BLAS library's default workspace unless ATen
workspace caching is explicitly enabled. When caching is disabled, internal
ATen operations may temporarily bind their own workspace to this handle, but
restore the default workspace before releasing it.

On ROCm, this function returns a different handle for each thread and
stream, and another one while the current stream is capturing. Run work on
a handle only on the stream it was returned for, and inside a capture call
this function again rather than use a handle obtained before it. See
[hipBLAS workspaces](../notes/hip.html#hipblas-workspaces) for the workspace each handle has, how handles
pass between threads, how to move one to another stream, and what to call
before graph capture begins.