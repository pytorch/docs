# torch.cuda.gds.is_available

torch.cuda.gds.is_available()[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/cuda/gds.py#L24)

Return `True` if GPUDirect Storage (GDS) support is built in.

This requires a Linux build with `USE_CUFILE` enabled (the default) and
with cuFile (CUDA) or hipFile (ROCm) available at build time. See
[hipFile (GPUDirect Storage)](../notes/hip.html#rocm-gds) for the ROCm requirements.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)