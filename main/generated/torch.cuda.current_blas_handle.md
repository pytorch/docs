# torch.cuda.current_blas_handle

torch.cuda.current_blas_handle()[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/cuda/__init__.py#L1449)

Return the `cublasHandle_t` pointer for the current device and stream.

On CUDA, the handle uses the BLAS library's default workspace unless ATen
workspace caching is explicitly enabled. When caching is disabled, internal
ATen operations may temporarily bind their own workspace to this handle, but
restore the default workspace before releasing it. On ROCm they use
separate handles, and this function returns a different handle for each
stream, because a rocBLAS workspace must not be shared by two streams at
once. Each is bound when it is created to a buffer from a caching-allocator
pool reserved for these buffers, at least as large as the workspace rocBLAS would allocate, which
rocBLAS never grows. A workspace bound with
`rocblas_set_workspace` stays bound, even after the thread exits and the
handle passes to another thread, so unbind it before freeing the buffer.
While the current stream is capturing, ROCm returns a capture handle
instead, bound to a workspace from the capture's memory pool: call this
function inside the capture rather than reusing a handle obtained before
it, and do not use the capture handle after the capture ends.