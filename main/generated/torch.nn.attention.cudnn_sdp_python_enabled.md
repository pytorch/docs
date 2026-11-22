# torch.nn.attention.cudnn_sdp_python_enabled

torch.nn.attention.cudnn_sdp_python_enabled()[[source]](https://github.com/pytorch/pytorch/blob/65e101a3cc8242711ae1cb467ed6cde097135821/torch/nn/attention/__init__.py#L216)

Warning

This API is beta and subject to change.

Returns whether [`enable_cudnn_sdp_python()`](torch.nn.attention.enable_cudnn_sdp_python.html#torch.nn.attention.enable_cudnn_sdp_python) has installed the cuDNN
frontend's implementation. Dense scaled dot product attention reaches it
only when the cuDNN backend is selected (see
[`torch.backends.cuda.enable_cudnn_sdp()`](../backends.html#torch.backends.cuda.enable_cudnn_sdp)). Every varlen call reaches
it, and it passes on the calls that did not select cuDNN. Either way, the
frontend passes configurations it does not support to the built-in C++
implementation.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)