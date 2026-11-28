# torch.nn.attention.enable_cudnn_sdp_python

torch.nn.attention.enable_cudnn_sdp_python(*enabled*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/nn/attention/__init__.py#L231)

Warning

This API is beta and subject to change.

Selects which implementation backs cuDNN scaled dot product attention: the
cuDNN frontend Python API when True, or the built-in C++ implementation
when False. Enabling requires `nvidia-cudnn-frontend>=1.32.3`. Its
`cudnn.torch` module is imported on the first enable and not before;
[`is_cudnn_sdp_python_available()`](torch.nn.attention.is_cudnn_sdp_python_available.html#torch.nn.attention.is_cudnn_sdp_python_available) imports only the `cudnn` package.

This chooses an *implementation*, so it is orthogonal to
[`torch.backends.cuda.enable_cudnn_sdp()`](../backends.html#torch.backends.cuda.enable_cudnn_sdp), which chooses whether the
cuDNN *backend* is eligible for selection at all: with that off, neither
implementation runs.

It replaces the CUDA kernels of `_scaled_dot_product_cudnn_attention`, its
backward, and the [`varlen_attn()`](../nn.attention.varlen.html#torch.nn.attention.varlen.varlen_attn) ops. The
varlen ops are shared with flash attention, so with this on every varlen
call reaches the frontend first; it serves the calls that selected cuDNN
and passes the rest to PyTorch's own kernels, so the active flash attention
implementation is unaffected. Nested-tensor inputs keep the built-in
implementation. So does dense SDPA in code that calls the CUDA kernels
without going through the dispatcher: AOTInductor and `torch.compile`
with `cpp_wrapper=True` call C shims for it, while the varlen ops there
still reach the frontend.