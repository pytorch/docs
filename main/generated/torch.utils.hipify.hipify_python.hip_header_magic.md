# torch.utils.hipify.hipify_python.hip_header_magic

torch.utils.hipify.hipify_python.hip_header_magic(*input_string*)[[source]](https://github.com/pytorch/pytorch/blob/3af07571b9d7402fd74352d079e6ff5fa307ec5f/torch/utils/hipify/hipify_python.py#L497)

If the file makes kernel builtin calls and does not include the cuda_runtime.h header,
then automatically add an #include to match the "magic" includes provided by NVCC.
.. todo:: Update logic to ignore cases where the cuda_runtime.h is included by another file.