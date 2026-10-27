# torch.utils.hipify.hipify_python.hip_header_magic

torch.utils.hipify.hipify_python.hip_header_magic(*input_string*)[[source]](https://github.com/pytorch/pytorch/blob/3d5976e3f87222f326a3b2c424828b74ec6cf594/torch/utils/hipify/hipify_python.py#L489)

If the file makes kernel builtin calls and does not include the cuda_runtime.h header,
then automatically add an #include to match the "magic" includes provided by NVCC.
.. todo:: Update logic to ignore cases where the cuda_runtime.h is included by another file.