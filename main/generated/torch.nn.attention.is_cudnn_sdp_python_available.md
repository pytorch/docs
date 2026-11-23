# torch.nn.attention.is_cudnn_sdp_python_available

torch.nn.attention.is_cudnn_sdp_python_available()[[source]](https://github.com/pytorch/pytorch/blob/e9565720ab4f59a0ed491b3f8440ae38c2455bab/torch/nn/attention/__init__.py#L202)

Warning

This API is beta and subject to change.

Returns whether `nvidia-cudnn-frontend`'s `cudnn.torch` module can be
found. It imports the `cudnn` package to look, but not `cudnn.torch`,
and does not check the version: [`enable_cudnn_sdp_python()`](torch.nn.attention.enable_cudnn_sdp_python.html#torch.nn.attention.enable_cudnn_sdp_python) still
raises if the installed package is older than it requires. An installed
`cudnn` package that fails to import is reported as unavailable;
[`enable_cudnn_sdp_python()`](torch.nn.attention.enable_cudnn_sdp_python.html#torch.nn.attention.enable_cudnn_sdp_python) raises the underlying error.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)