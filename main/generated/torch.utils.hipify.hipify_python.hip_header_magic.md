# torch.utils.hipify.hipify_python.hip_header_magic

torch.utils.hipify.hipify_python.hip_header_magic(*input_string*)[[source]](https://github.com/pytorch/pytorch/blob/502e93eb52e0fcf07a908796ccd61af06c4b58b9/torch/utils/hipify/hipify_python.py#L497)

If the file makes kernel builtin calls and does not include the cuda_runtime.h header,
then automatically add an #include to match the "magic" includes provided by NVCC.
.. todo:: Update logic to ignore cases where the cuda_runtime.h is included by another file.