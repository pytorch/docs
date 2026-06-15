# torch.utils.hipify.hipify_python.hip_header_magic

torch.utils.hipify.hipify_python.hip_header_magic(*input_string*)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/utils/hipify/hipify_python.py#L497)

If the file makes kernel builtin calls and does not include the cuda_runtime.h header,
then automatically add an #include to match the "magic" includes provided by NVCC.
.. todo:: Update logic to ignore cases where the cuda_runtime.h is included by another file.