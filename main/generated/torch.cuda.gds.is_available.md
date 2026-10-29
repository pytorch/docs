# torch.cuda.gds.is_available

torch.cuda.gds.is_available()[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/cuda/gds.py#L24)

Return `True` if GPUDirect Storage (GDS) support is built in.

This requires a Linux build with `USE_CUFILE` enabled (the default) and
with cuFile (CUDA) or hipFile (ROCm) available at build time. See
[hipFile (GPUDirect Storage)](../notes/hip.html#rocm-gds) for the ROCm requirements.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)